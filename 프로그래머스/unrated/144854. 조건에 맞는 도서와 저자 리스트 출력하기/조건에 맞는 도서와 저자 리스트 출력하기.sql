-- 코드를 입력하세요
SELECT book_id, author_name, date_format(published_date,'%Y-%m-%d') as PUBLISHED_DATE
from book
natural join author
where category = '경제'
order by published_date;