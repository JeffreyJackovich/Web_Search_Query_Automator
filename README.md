# web_search_query_automator

Automates a Google Web Search Query via the following process:  

  Reads Strings in a designated CSV, perform a Google web search query, and returns respective URL's in descending SEO order (beginning with the highest ranking url) to the designated CSV row.   

Requirements:

  1. A CSV (EX: "query_results.csv") with indicated headers (see Example file headers below):
    
    Row 1, Column A: "Fruit"
    Row 2, Column B: "Link1"
    Row 3, Column C: "Link2"
  2. Web search queries in descending cells (Example: "Best Organic Apples in Brooklyn" in column A, row 2; "Best Organic  Apples in Queens" in column A, row 3, etc) from the indicated header (default Example: "Fruit").
  3. Desired URL location indicated in the header row (Example: "Link1", "Link2").

To Note:

   Keep, "pause" (line:17) at 5.0. 
   Shorter than 5.0 results in a, "503 Service Temporarily Unavailable" error.

To modify the number of returned urls:

   Increase or decrease the number on: line 9. 
   Per number of desired urls, add the appropriate header row title at lines: 12 and 18.

Program Duration:

   ~20 minutes via the following parameters:
      176 rows, 3 links (per row), pause=5.0
