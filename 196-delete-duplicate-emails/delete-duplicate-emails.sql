with cte as (
    select id, email, row_number() over(partition by email order by id) rn
    from Person
)
delete 
from Person
where id in (select id from cte where rn > 1)