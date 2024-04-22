import scrapy
from bs4 import BeautifulSoup
import re
from CSCoursesCrawler.items import CscoursescrawlerItem  # Make sure to define CourseItem in your items.py

class CollegeCoursesSpider(scrapy.Spider):
    name = 'college_courses'
    allowed_domains = ['bulletin.iit.edu']  # Change to your college's domain
    start_urls = ['https://bulletin.iit.edu/graduate/courses/cs/']  # The actual URL



    def parse(self, response):
        # Inspect the structure of the webpage and adjust selectors accordingly
        courses = response.xpath('//div[@class="courseblock"]').getall()   
        
        for course in courses:
            print("printing item\n")
            course_code = ""
            course_title = ""
            course_description = ""
            prerequisites=""
            lecture_hours = ""
            lab_hours = ""
            credits = ""

            # Parse the HTML content
            soup = BeautifulSoup(course, 'html.parser')
            try:
                # Extract data
                course_code = soup.find("div", class_="coursecode").text.strip()
                course_title = soup.find("div", class_="coursetitle").strong.text.strip()
                course_description = soup.find("div", class_="courseblockdesc").p.text.strip()
                try: 
                    prerequisites = soup.find("div", class_="noindent courseblockattr").text.strip()
                except:
                    print()
                
                lecture_hours = soup.select_one("span:contains('Lecture:')").text.strip()
                lab_hours = soup.select_one("span:contains('Lab:')").text.strip()
                credits = soup.select_one("span:contains('Credits:')").text.strip()
                
                print(course_code)
                print(course_title)
                print(course_description)
                print(prerequisites)
                print(lecture_hours)
                print(lab_hours)
                print(credits)
                # return
                item = CscoursescrawlerItem()
                item['code'] = course_code.replace('\xa0', ' ')
                item['title'] = course_title
                item['description'] = course_description
                item['prerequisites'] = prerequisites
                item ['lecture'] = lecture_hours
                item ['lab'] = lab_hours
                item ['credits'] = credits

                yield item
            except:
                print()
    
