from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.web_scraping import WebScraping
from pysummarization.abstractabledoc.std_abstractor import StdAbstractor
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


#  # Object of web scraping.
# web_scrape = WebScraping()
#     # Web-scraping.
# document = web_scrape.scrape("https://en.wikipedia.org/wiki/Internet_of_things")

def Main(document):
    '''
    Entry point.
    
    Args:
        url:    target url.
    '''
   

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter.
    auto_abstractor.delimiter_list = [".", ","]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(document, abstractable_doc)
    return result_dict
    # # Output 3 summarized sentences.
    # limit = 3
    # i = 1
    # for sentence in result_dict["summarize_result"]:
    #     print(sentence)
    #     if i >= limit:
    #         break
    #     i += 1

if __name__ == "__main__":
    import sys
    # web site url.
    url = sys.argv[1]
    # Object of web scraping.
    web_scrape = WebScraping()
        # Web-scraping.
    # document = web_scrape.scrape("https://en.wikipedia.org/wiki/Internet_of_things")
    # Main(document)