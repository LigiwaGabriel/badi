

import json
import os
import datetime


FACTORY_TAX_RATE      = 0.25   # 25% of annual income
SME_TAX_RATE          = 0.15   # 15% of annual income
DOMESTIC_TAX_RATE     = 0.03   # 3% per transaction

DATA_FILE    = "ura_taxpayers.json"
REVENUE_DIR  = "revenue_files"


def load_data():
    """Load taxpayer records from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    """Save taxpayer records to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def compute_factory_tax(annual_income: float) -> float:
    """Calculate tax for a factory (25% of annual income)."""
    return round(annual_income * FACTORY_TAX_RATE, 2)


def compute_sme_tax(annual_income: float) -> float:
    """Calculate tax for an SME (15% of annual income)."""
    return round(annual_income * SME_TAX_RATE, 2)


def compute_domestic_tax(transactions: list) -> float:
    """
    Calculate tax for a domestic trader (3% per transaction).
    transactions: list of transaction amounts (floats)
    """
    total = sum(transactions)
    return round(total * DOMESTIC_TAX_RATE, 2)



def register_taxpayer(data: dict) -> dict:
    """Register a new taxpayer interactively."""
    print("\n--- Register New Taxpayer ---")
    tin = input("Enter TIN (Taxpayer Identification Number): ").strip()
    if tin in data:
        print(f"  [!] TIN '{tin}' already exists.")
        return data

    name = input("Enter taxpayer name: ").strip()
    print("  Taxpayer types:")
    print("    1 - Factory")
    print("    2 - SME (Small & Medium Enterprise)")
    print("    3 - Domestic Trader")
    choice = input("  Select type (1/2/3): ").strip()

    type_map = {"1": "factory", "2": "sme", "3": "domestic"}
    if choice not in type_map:
        print("  [!] Invalid type selected.")
        return data

    taxpayer_type = type_map[choice]
    data[tin] = {
        "name": name,
        "type": taxpayer_type,
        "tax_records": []          # list of yearly records
    }
    save_data(data)
    print(f"  [✓] Taxpayer '{name}' registered with TIN '{tin}'.")
    return data


def file_tax(data: dict) -> dict:
    """File a tax return for an existing taxpayer."""
    print("\n--- File Tax Return ---")
    tin = input("Enter TIN: ").strip()
    if tin not in data:
        print("  [!] Taxpayer not found.")
        return data

    taxpayer = data[tin]
    year = input("Enter tax year (e.g. 2024): ").strip()

    # Check for duplicate filing
    for rec in taxpayer["tax_records"]:
        if rec["year"] == year:
            print(f"  [!] Tax already filed for {year}.")
            return data

    tp_type = taxpayer["type"]
    record = {"year": year}

    if tp_type == "factory":
        income = float(input("  Enter annual income (UGX): "))
        tax    = compute_factory_tax(income)
        record.update({"income": income, "tax_due": tax, "rate": "25%"})

    elif tp_type == "sme":
        income = float(input("  Enter annual income (UGX): "))
        tax    = compute_sme_tax(income)
        record.update({"income": income, "tax_due": tax, "rate": "15%"})

    elif tp_type == "domestic":
        print("  Enter transaction amounts one by one.")
        print("  (Press ENTER with no value when done)")
        transactions = []
        while True:
            val = input(f"  Transaction {len(transactions)+1} amount: ").strip()
            if val == "":
                break
            try:
                transactions.append(float(val))
            except ValueError:
                print("  [!] Invalid amount — skipped.")
        tax = compute_domestic_tax(transactions)
        record.update({
            "transactions": transactions,
            "total_sales": round(sum(transactions), 2),
            "tax_due": tax,
            "rate": "3% per transaction"
        })

    taxpayer["tax_records"].append(record)
    save_data(data)
    print(f"\n  [✓] Tax filed for {taxpayer['name']} ({year})")
    print(f"      Tax Due: UGX {record['tax_due']:,.2f}")
    return data


def view_taxpayer(data: dict):
    """Display full profile and tax history for a taxpayer."""
    print("\n--- Taxpayer Profile ---")
    tin = input("Enter TIN: ").strip()
    if tin not in data:
        print("  [!] Taxpayer not found.")
        return

    tp = data[tin]
    print(f"\n  Name : {tp['name']}")
    print(f"  TIN  : {tin}")
    print(f"  Type : {tp['type'].upper()}")
    print(f"  {'─'*40}")

    if not tp["tax_records"]:
        print("  No tax records found.")
        return

    total_tax = 0
    for rec in tp["tax_records"]:
        print(f"\n  Year : {rec['year']}")
        print(f"  Rate : {rec['rate']}")
        if "income" in rec:
            print(f"  Annual Income : UGX {rec['income']:,.2f}")
        if "total_sales" in rec:
            print(f"  Total Sales   : UGX {rec['total_sales']:,.2f}")
            print(f"  Transactions  : {len(rec['transactions'])}")
        print(f"  Tax Due       : UGX {rec['tax_due']:,.2f}")
        total_tax += rec["tax_due"]

    print(f"\n  {'─'*40}")
    print(f"  Total Tax Paid : UGX {total_tax:,.2f}")


def generate_revenue_report(data: dict):
    """
    Compute total revenue collected by URA for a given year
    and save it to a revenue file.
    """
    print("\n--- Generate Annual Revenue Report ---")
    year = input("Enter year: ").strip()

    factory_total  = 0.0
    sme_total      = 0.0
    domestic_total = 0.0
    contributors   = []

    for tin, tp in data.items():
        for rec in tp["tax_records"]:
            if rec["year"] == year:
                tax = rec["tax_due"]
                contributors.append({
                    "tin": tin,
                    "name": tp["name"],
                    "type": tp["type"],
                    "tax": tax
                })
                if tp["type"] == "factory":
                    factory_total += tax
                elif tp["type"] == "sme":
                    sme_total += tax
                elif tp["type"] == "domestic":
                    domestic_total += tax

    grand_total = factory_total + sme_total + domestic_total

    # Build report content
    report_lines = [
        "=" * 60,
        "       UGANDA REVENUE AUTHORITY",
        f"       ANNUAL REVENUE REPORT — {year}",
        "=" * 60,
        f"  Generated : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "  REVENUE BY SECTOR",
        "  " + "-" * 40,
        f"  Factories (25%)   : UGX {factory_total:>15,.2f}",
        f"  SMEs      (15%)   : UGX {sme_total:>15,.2f}",
        f"  Domestic  ( 3%)   : UGX {domestic_total:>15,.2f}",
        "  " + "-" * 40,
        f"  GRAND TOTAL       : UGX {grand_total:>15,.2f}",
        "",
        "  INDIVIDUAL CONTRIBUTORS",
        "  " + "-" * 40,
    ]

    for c in contributors:
        report_lines.append(
            f"  {c['tin']:<12} {c['name']:<20} {c['type']:<10} UGX {c['tax']:>12,.2f}"
        )

    report_lines += [
        "=" * 60,
        f"  Total Taxpayers Filed : {len(contributors)}",
        "=" * 60,
    ]

    report_text = "\n".join(report_lines)

    # Save to revenue_files directory
    os.makedirs(REVENUE_DIR, exist_ok=True)
    filename = os.path.join(REVENUE_DIR, f"revenue_{year}.txt")
    with open(filename, "w") as f:
        f.write(report_text)

    print(report_text)
    print(f"\n  [✓] Report saved to: {filename}")



def list_taxpayers(data: dict):
    """Display a summary table of all registered taxpayers."""
    print("\n--- Registered Taxpayers ---")
    if not data:
        print("  No taxpayers registered yet.")
        return

    print(f"\n  {'TIN':<12} {'Name':<25} {'Type':<12} {'Records'}")
    print("  " + "-" * 55)
    for tin, tp in data.items():
        print(
            f"  {tin:<12} {tp['name']:<25} {tp['type']:<12} "
            f"{len(tp['tax_records'])} year(s)"
        )



def search_taxpayer(data: dict):
    """Search taxpayers by name (partial match)."""
    print("\n--- Search Taxpayer ---")
    query = input("Enter name to search: ").strip().lower()
    found = {
        tin: tp for tin, tp in data.items()
        if query in tp["name"].lower()
    }
    if not found:
        print("  No matching taxpayers found.")
    else:
        print(f"\n  Found {len(found)} result(s):")
        for tin, tp in found.items():
            print(f"  TIN: {tin} | Name: {tp['name']} | Type: {tp['type'].upper()}")


def main():
    data = load_data()

    menu = """
╔══════════════════════════════════════════════╗
║       UGANDA REVENUE AUTHORITY (URA)         ║
║         Tax Management System                ║
╠══════════════════════════════════════════════╣
║  1. Register New Taxpayer                    ║
║  2. File Tax Return                          ║
║  3. View Taxpayer Profile                    ║
║  4. List All Taxpayers                       ║
║  5. Search Taxpayer by Name                  ║
║  6. Generate Annual Revenue Report           ║
║  0. Exit                                     ║
╚══════════════════════════════════════════════╝
"""

    while True:
        print(menu)
        choice = input("  Select option: ").strip()

        if choice == "1":
            data = register_taxpayer(data)
        elif choice == "2":
            data = file_tax(data)
        elif choice == "3":
            view_taxpayer(data)
        elif choice == "4":
            list_taxpayers(data)
        elif choice == "5":
            search_taxpayer(data)
        elif choice == "6":
            generate_revenue_report(data)
        elif choice == "0":
            print("\n  Goodbye. URA session ended.\n")
            break
        else:
            print("  [!] Invalid option. Please try again.")



if __name__ == "__main__":
    main()
    
