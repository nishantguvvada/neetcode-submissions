class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''.join([f'{len(i)}#{i}' for i in strs])
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        pointer = 0
        result = []
        while pointer < len(s):
            hash_index = s.find('#', pointer)

            str_len = int(s[pointer: hash_index])

            result.append(s[hash_index+1:hash_index+str_len+1])

            pointer = hash_index + str_len + 1
        return result