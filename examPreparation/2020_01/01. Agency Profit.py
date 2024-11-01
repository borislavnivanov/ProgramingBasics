AGENCY_MARGIN = 0.20

company_name = input()
tickets_adult = int(input())
tickets_kids = int(input())
price_ticket_adult = float(input())
price_ticket_kids = price_ticket_adult * 0.30
price_service = float(input())

total_revenue = 0.00

total_revenue += tickets_adult * price_ticket_adult
total_revenue += tickets_kids * price_ticket_kids
total_revenue += price_service * (tickets_kids + tickets_adult)
total_revenue *= AGENCY_MARGIN

print(f'The profit of your agency from {company_name} tickets is {total_revenue:.2f} lv.')
