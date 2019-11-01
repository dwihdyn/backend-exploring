website : https://next-sql.netlify.com/basic

1) 
select politician_id, count(*) as num_votes from votes
where politician_id = 524


2)
select cm.name, count(*) as num_votes
from votes as v join congress_members as cm 
on (v.politician_id = cm.id)
where cm.id = 524


3) 
select cm.name, count(*) as num_votes
from votes as v join congress_members as cm on (v.politician_id = cm.id)
where politician_id = 339

*4) 
select cm.name, count(*) as num_votes
from votes as v left join congress_members as cm on (v.politician_id = cm.id)
group by 1
order by 2 desc

* answer is the same the expected output, but the names are in different order for each level





*5)
select cm.name, count(*) as num_votes
from votes as v left join congress_members as cm
on (v.politician_id = cm.id)
group by 1
order by 2

* for politician Rep. Mike Rogers, there are 29 votes when we call it out, but in expected output only shows 6 votes