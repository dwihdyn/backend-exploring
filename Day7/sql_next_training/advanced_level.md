website : https://next-sql.netlify.com/advanced

1)
select cm.name, count(*) as votes
from congress_members as cm  join votes as v on (v.politician_id = cm.id)
group by 1
order by 2 desc
limit 1


2)
select vo.first_name, vo.last_name, vo.party, vo.gender,cm.name
from congress_members as cm  join votes as v 
on (v.politician_id = cm.id)
join voters as vo 
on (v.voter_id = vo.id)
where cm.name = 'Rep. Dan Benishek'


3)
select cm.name, cm.location, cm.grade_1996, count(*) as num_votes
from congress_members as cm  join votes as v on (v.politician_id = cm.id)
where cm.grade_current < 9
group by 1
order by 3


4)
select cm.location, count(*) as num_voters
from congress_members as cm  join votes as v on (v.politician_id = cm.id)
group by 1
order by 2 desc
limit 10


5)
select vo.first_name, vo.last_name, vo.gender, vo.party, vo.age, cm.location
from congress_members as cm  join votes as v 
on (v.politician_id = cm.id)
join voters as vo 
on (v.voter_id = vo.id)
where cm.location in 
(
    SELECT loc from
    (
        select cm.location as loc, count(*) as num_voters
        from congress_members as cm  join votes as v on (v.politician_id = cm.id)
        group by 1
        order by 2 desc
        limit 10
    )
)



6)
select * 
from
(
    select 
    vo.first_name, 
    vo.last_name, 
    v.voter_id,
    COUNT(*)
    from votes as v
    join voters as vo 
    on (v.voter_id = vo.id)
    group by 3
    having COUNT(*) > 2
    order by 3
)


7)
SELECT 
v.id as votes_id,
first_name as voter_first_name, 
last_name as voter_last_name,  
name as politician_name, 
COUNT(*) as votes_no

FROM votes as v JOIN congress_members 
ON politician_id = congress_members.id

JOIN voters 
ON voter_id = voters.id
GROUP BY first_name, last_name, name
HAVING votes_no > 1
ORDER BY voter_id