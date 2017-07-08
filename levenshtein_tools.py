import Levenshtein
import pyperclip


class LevenshteinList:
    # https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html
    @staticmethod
    def process_returns_to_list(text_list):
        # strip \x00 = end of transmission, return a list of items
        return text_list.split('\x00')[0].split('\r\n')

    @staticmethod
    def find_best_string_match(item, list_possibilities):
        best_match = ''
        best_score = 1000
        for poss in list_possibilities:
            if not poss:
                continue
            current_score = Levenshtein.distance(item, poss)
            if current_score == 0:
                return poss, 0
            if current_score <= best_score:
                best_score = current_score
                best_match = poss
        return best_match, best_score

    def process_lists(self, list_possibilities, list_to_process):
        results = []
        for item in list_to_process:
            if not item:
                continue
            best_match, best_score = self.find_best_string_match(item, list_possibilities)
            results.append([item, best_match, best_score])
        return results


def main():
    lev = LevenshteinList()
    input('Copy source list and press Enter when ready.')
    list_possibilities = pyperclip.paste().split('\x00')[0].splitlines()  # \x00 = end of transmission
    # print(list_possibilities)
    input('Source list saved.\nCopy list to process and press Enter when ready.')
    list_to_process = lev.process_returns_to_list(pyperclip.paste())
    # print(list_to_process)
    result = lev.process_lists(list_possibilities, list_to_process)
    result_str = '\n'.join('\t'.join(str(y) for y in x) for x in result)
    # print(*list, sep='\t') is also quite nice if you're printing
    # print(result_str)
    pyperclip.copy(result_str)

main()
