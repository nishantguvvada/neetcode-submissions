class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for el in strs:
            val = str(len(el)) + '#' + el
            encoded_str += val
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            decoded_str.append(s[j+1:j+1+length])
            i = j+1+length

        return decoded_str
