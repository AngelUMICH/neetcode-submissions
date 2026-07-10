class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> seen;
        for (const auto& s: strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            seen[sortedS].push_back(s);
        }
        vector<vector<string>> result;
        for (auto& p : seen) {
            result.push_back(p.second);
        }
        return result;
    }
};
