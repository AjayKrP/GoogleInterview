class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = len(a) - 1
        r = len(b) - 1

        carry, out = divmod(int(a[l]) + int(b[r]), 2)

        result = [out]
        l -= 1
        r -= 1

        while l >= 0 or r >= 0:
            v1 = int(a[l]) if l >= 0 else 0
            v2 = int(a[r]) if r >= 0 else 0
            carry, out = divmod(v2 + v1 + carry, 2)
            result.append(out)
            l -= 1
            r -= 1
        if carry > 0:
            result.append(carry)
        result.reverse()
        res = ''.join([f'{w}' for w in result])
        return res


sol = Solution()
print(sol.addBinary('11', '1'))

import json


def json_max_depth(obj):
    if type(obj) is dict:
        if len(obj) == 0:
            return 1
        return 1 + max(json_max_depth(obj[x]) for x in obj)
    if type(obj) is list:
        if len(obj) == 0:
            return 1
        return 1 + max(json_max_depth(x) for x in obj)
    return 0


def test_json_max_depth():
    assert json_max_depth(json.loads('[[[[]]]]')) == 4
    assert json_max_depth(json.loads('{"a":{"v":"123"}}')) == 2
    assert json_max_depth(json.loads('{"product":{"item":{"name": "mango"}}}')) == 3


def find_inorder_preorder_to_postorder():
    pass
