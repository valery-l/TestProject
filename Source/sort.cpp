#include <fstream>
#include <vector>

using namespace std;
           
void mega_sort(vector<int>& v)
{
    for (size_t i = 0; i < v.size() - 1; ++i)
        for (size_t j = 0; j < v.size() - 1 - i; ++j)
            if (v[j] > v[j + 1])
                swap(v[j], v[j + 1]);
}

void print_out(ostream& out, vector<int>& v)
{
    for (auto item : v)
        out << item << " ";

    out << endl;
}

int main() 
{
    ifstream is("input.txt");
    ofstream os("output.txt");

    vector<int> numbers;
    while (!is.eof())
    { 
        int num;
        if (is >> num)
            numbers.push_back(num);
    }

    mega_sort(numbers);
    print_out(os, numbers);

    return 0;
}
