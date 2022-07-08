-- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT score, number FROM second_table WHERE score, number NOT IN (SELECT DISTINCT score, number FROM second_table WHERE name="YES");
