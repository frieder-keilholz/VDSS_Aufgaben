Aufgabe 3
Wie viele ToDos je Nutzer gibt es?

- Command:
  db.test3.aggregate( [ { $group: {"_id": "$user", "No_of_Times": { $sum: 1  } } } ] );
- Output:
{ "_id" : "Tammy Stevens", "No_of_Times" : 10 }
{ "_id" : "Brandi Stein", "No_of_Times" : 4 }
{ "_id" : "Kevin Moore", "No_of_Times" : 7 }
{ "_id" : "Meredith Daniels", "No_of_Times" : 2 }
{ "_id" : "Lydia Allen MD", "No_of_Times" : 8 }
{ "_id" : "Sierra Newman", "No_of_Times" : 8 }
{ "_id" : "Yesenia Cobb", "No_of_Times" : 3 }
{ "_id" : "Patricia Phelps", "No_of_Times" : 2 }
{ "_id" : "John Spencer Jr.", "No_of_Times" : 10 }
{ "_id" : "Susan Smith", "No_of_Times" : 9 }
{ "_id" : "Lisa Jones", "No_of_Times" : 4 }
{ "_id" : "Sean Stone", "No_of_Times" : 7 }
{ "_id" : "Anna Gray", "No_of_Times" : 10 }
{ "_id" : "Stephanie Miles", "No_of_Times" : 5 }
{ "_id" : "Joshua Thomas", "No_of_Times" : 8 }
{ "_id" : "Aaron Chase", "No_of_Times" : 1 }
{ "_id" : "Kyle Morales", "No_of_Times" : 2 }
{ "_id" : "Donald Anderson", "No_of_Times" : 8 }
{ "_id" : "William Hernandez", "No_of_Times" : 6 }
{ "_id" : "Eric Patterson", "No_of_Times" : 5 }

