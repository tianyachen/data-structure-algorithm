with RankedEmployee as (
    select
        id,
        name,
        salary,
        departmentId,
        dense_rank() over (
            partition by departmentId
            order by salary desc
        ) as salary_rank
    from Employee
)
select 
    Department.name as Department,
    RankedEmployee.name as Employee,
    RankedEmployee.salary as Salary
from RankedEmployee
inner join Department
    on RankedEmployee.DepartmentId = Department.id
where RankedEmployee.salary_rank <=3;