# gitmermaid

GitMermaid generates branch graph diagrams of your git repository using 
[mermaid](https://github.com/knsv/mermaid). The script currently supports
generation of input diagram code, which can be visualised
[here](http://www.naseer.in/mermaid-webapp/).

# example output

    graph TD;
    5db803f[Shorten hashes and remove tabs] --> fc304c5
    fc304c5[Add README] --> 4f5a152
    4f5a152[Initial features] --> 38e4299
    4f5a152[Initial features] --> b54cae4
    b54cae4[Implement writing mermaid instructions to file] --> 9e8fe09
    9e8fe09[Fix script to work] --> 38e4299
    38e4299[Rewrite and clean up script] --> 736447b
    736447b[Initial commit with initial tool] --> root
