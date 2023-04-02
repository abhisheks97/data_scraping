The Application of this Django Project is to scrap the data from amazon based on the user required keyword.


Requirements stored in : requirements.txt

Command to RUN the server: python manage.py runserver (in root project directory)

User API to search any keyword and get the data from amazon: http://127.0.0.1:8000/amazon/get_data/?keyw=mobiles

Example Output contains:

{"product_data": [{"title": "Samsung Galaxy M04 Light Green, 4GB RAM, 128GB Storage | Upto 8GB RAM with RAM Plus |
MediaTek Helio P35 | 5000 mAh Battery", "url": "
/sspa/click?ie=UTF8&spc=MTo1MzU5NzIwMDgyMjQ0OTMxOjE2ODA0MzI2MjA6c3BfYXRmOjIwMTAzNjkzMjc5Nzk4OjowOjo&url=%2FSamsung-Galaxy-Storage-MediaTek-Battery%2Fdp%2FB0BMGC6LHP%2Fref%3Dsr_1_1_sspa%3Fkeywords%3Dmobiles%26qid%3D1680432620%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "
rating": "3.9 out of 5 stars", "reviews": null, "price": "\u20b910,249", "
search_url": "https://www.amazon.in/s?k=mobiles"}, {"title": "Redmi Note 12 5G Matte Black 6GB RAM 128GB ROM | 1st Phone
with 120Hz Super AMOLED and Snapdragon\u00ae 4 Gen 1 | 48MP AI Triple Camera", "url": "
/sspa/click?ie=UTF8&spc=MTo1MzU5NzIwMDgyMjQ0OTMxOjE2ODA0MzI2MjA6c3BfYXRmOjIwMTA5MjI1NjU0MDk4OjowOjo&url=%2FRedmi-AMOLED-Snapdragon%25C2%25AE-Triple-Camera%2Fdp%2FB0BQ3MT8P2%2Fref%3Dsr_1_2_sspa%3Fkeywords%3Dmobiles%26qid%3D1680432620%26sr%3D8-2-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "
rating": "3.9 out of 5 stars", "reviews": null, "price": "\u20b919,999", "
search_url": "https://www.amazon.in/s?k=mobiles"}, "error": false, "msg": ""}


API also stored the scraped data in "results.json" file in directory: "/data_scraping/amazon"


selectorlib (https://pypi.org/project/selectorlib/) is the tool used for Data scraping.

Project Structure:

  - amazon application created in project data_scraping which is responsible to scrap data from Amazon
