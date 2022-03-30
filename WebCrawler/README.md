# Specialized Web Crawler

## Description

## Pre-requisites

## Installation


## Checklist

1. [25%] Implement your crawler according to requirements

  - [ ] (a) Describe the key architecture of my web crawler.
  - [ ] (b) Identify & describe the major data structures used (lists, arrays, etc).
  - [ ] (c) Describe how "politeness" was implemented within my crawler.
  - [ ] (d) Describe in detail how (c) is implemented within my code.

2. [20%] Use my crawler to determine & save the URL, <TITLE>, date & size of all pages in the test data.
Provide a listing of this information as well as all links going out of the test data (i.e. items you must not crawl).

  - [ ] Completed?

3. [10%] Implement exact duplicate content detection. List the URLs of pages that contain already seen content.
Don't index the duplicate pages.

  - [ ] Completed?

4. [10%] Use my crawler to list all broken links within the test data.

  - [ ] Completed?

5. [10%] List the URLs of non-text files that are referenced in the test data.

  - [ ] Completed?

6. [25%] My crawler must save each word & position from each text file of type (.txt, .htm, .html, .php).
Make sure that I don't save HTML markup. Unless I provide a different definition, I can assume a word is a string
of non-space character(s), beginning w/ an alphabetic character. If a token does not begin w/ an alphabetic character,
remove those until it's alphabetic or null. I can decide if it can contain special characters, but the last character
of a word is either alphabetic or numeric. Perform case insensitive matching. Start w/ an empty dictionary & add words
as they are encountered. In this process, give each page a unique document ID. Further, the output of this step will
generate a term-document frequency matrix. My program may generate the data to be further processed in a spreadsheet (Excel or equivalent).

  - [ ] (a) What is your definition of “word”?
  - [ ] (b) How many documents are indexed?
  - [ ] (c) How many words are indexed?
  - [ ] (d) Generate the term-document frequency matrix
