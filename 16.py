n = int(input())
tickets = []
for _ in range(n):
    ticket = input()
    if ticket.startswith('a') and ticket.endswith('55661'):
        tickets.append(ticket)

if len(tickets) == 0:
    print(-1)
else:
    print(' '.join(tickets))
