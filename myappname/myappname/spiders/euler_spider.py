# Cemre ACAR - www.cemreacar.com
import scrapy

class EulerSpider(scrapy.Spider):
    name = "problems"
    mypage = 2
    problem_count = 1
    file = open("problems.txt","a",encoding = "UTF-8")
    start_urls = [
        "https://projecteuler.net/archives;page=1"
    ]

    def parse(self, response):
        mytext = response.css("table#problems_table a").extract()
        problem_names = [u''.join(mytext.css('::text').extract()).strip() for mytext in response.css("table#problems_table a")]
        problem_solved_count = response.css("table#problems_table div::text").extract()


        i = 0
        while (i < len(problem_names)):
            """yield {
                "problem" : problem_names[i],
                "solved" : problem_solved_count[i],
            }"""

            self.file.write("-----------------------------------------------\n")
            self.file.write(str(self.problem_count) + ".\n")
            self.file.write("Problem İsmi : " + problem_names[i] + "\n")
            self.file.write("Çözüm Sayısı : " + problem_solved_count[i] + "\n")
            self.file.write("-----------------------------------------------\n")
            self.problem_count += 1


            i += 1
        next_url = "https://projecteuler.net/archives;page={}".format(self.mypage)
        self.mypage += 1

        if self.mypage != 5:
            yield scrapy.Request(url = next_url,callback = self.parse)
        else:
            self.file.close()
