-- with cte as (
--     select id, email, row_number() over(partition by email order by id) rn
--     from Person
-- )
-- delete 
-- from Person
-- where id in (select id from cte where rn > 1)

delete p1
from Person p1 join Person p2
on p1.email = p2.email and p1.id > p2.id;