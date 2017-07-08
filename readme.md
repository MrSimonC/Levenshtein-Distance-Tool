# Levenshtein Distance Tool
The [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) can help find text entries which are similar.

I've created this tool which takes an original list, then an "input" list, then using levenshtein distance, find the closest entry in the original list for each entry in the input list.

Output: copies the target list, closest "original" list entry, and levenshtein distance score to the clipboard, ready for pasting into Excel.

## Prerequisite
Install "Visual C++ Redistributable for Visual Studio 2015 x86.exe" (on 32-bit, or x64 on 64-bit) which allows Python 3.5 dlls to work, found here:
https://www.microsoft.com/en-gb/download/details.aspx?id=48145

## Installation and Running
In windows command line, run (found in binary folder) `leven.exe` and follow the instructions.