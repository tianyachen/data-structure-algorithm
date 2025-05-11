select today.id
from Weather today inner join Weather yesterday
on today.recordDate = adddate(yesterday.recordDate, 1)
where today.temperature > yesterday.temperature
