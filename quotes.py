from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.graph_objects as plotly


url = 'http://quotes.toscrape.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

quote_data = {}
author_data = {}
tag_data = {}

for page_num in range(1,11):
    updated_url = f"{url}page/{page_num}/"
    req = Request(updated_url, headers = headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    quotes = soup.findAll(class_ = "quote")


#Author Statistics
    for quote in quotes:
        text = quote.find('span', class_ = "text").text
        author = quote.find('small', class_ = "author").text
        tags = [tag.text for tag in quote.findAll('a', class_ = "tag")]

        author_data[author] = author_data.get(author, 0) + 1
        quote_data[text] = len(text)

        for tag in tags:
            tag_data[tag] = tag_data.get(tag, 0) + 1
    for author in author_data:
        print(f"{author} has {author_data[author]} featured quote(s)")


author_most_quotes = max(author_data, key=author_data.get)
author_least_quotes = min(author_data, key=author_data.get)

print("-" * 50)
print(f"Author with most featured quotes: {author_most_quotes}")
print(f"Author with least featured quotes: {author_least_quotes}")


#Quote Analysis
quote_total = len(quote_data)
quote_len = sum(quote_data.values())
len_of_quotes = quote_len / quote_total

longest_quote = max(quote_data, key=quote_data.get)
shortest_quote = min(quote_data, key=quote_data.get)

print("-" * 50)
print(f"The average length of quotes: {len_of_quotes} words")
print(f"The longest quote: {longest_quote}")
print(f"The shortest quote: {shortest_quote}")


#Tag Analysis
most_popular_tag = max(tag_data, key=tag_data.get)
total_tags = sum(tag_data.values()) #TOTAL QUOTES OVERALL
#total_tags = len(tag_data) #UNIQUE QUOTES

print("-" * 50)
print(f"The most popular tag: {most_popular_tag}")
print(f"Total tags used: {total_tags}")


#Visualization
hilo_authors = sorted(author_data.items(), key=lambda x: x[1], reverse=True)[:10]
p_authors= [item[0] for item in hilo_authors]                                                                            
p_quotes = [item[1] for item in hilo_authors]    

plot_authors = plotly.Figure(data=[plotly.Bar(x=p_authors, y=p_quotes)])
plot_authors.update_layout(title="Top 10 Authors", xaxis_title = "Quotes by Authors", yaxis_title = "Number of Quotes")
plot_authors.show()

hilo_tags = sorted(tag_data.items(), key=lambda x: x[1], reverse=True)[:10]
p_tags= [item[0] for item in hilo_tags]                                                                            
p_count = [item[1] for item in hilo_tags]    

plot_tags = plotly.Figure(data=[plotly.Bar(x=p_tags, y=p_count)])
plot_tags.update_layout(title="Top 10 Tags", xaxis_title = "Most popular tags by Authors", yaxis_title = "Count")
plot_tags.show()