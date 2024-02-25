#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

void bfs(unordered_map< string, vector< string > >& graph,
             string src)
{
    vector< string > queue{ src };

    while (!queue.empty())
    {
        string currNode = queue.back();
        queue.pop_back();

        for (auto& neighbour : graph.at(currNode))
            queue.insert(queue.begin(), neighbour);
    
        cout << "currNode : " << currNode << "\n";
    }
}

void dfsRec(unordered_map< string, vector< string > >& graph,
             string src)
{
    
    cout << "currNode: " << src << "\n";

    for (auto& neighbour : graph.at(src))
        dfsRec(graph, neighbour);
    
}

void dfsIter(unordered_map< string, vector< string > >& graph,
             string src)
{
    vector < string > stack { src };

    while (!stack.empty())
    {
        string currNode = stack.back();
        stack.pop_back();
        for (auto& neighbour : graph.at(currNode))
            stack.push_back(neighbour);

        cout << "currNode: " << currNode << "\n";
    }
}

int main()
{
    unordered_map< string, vector< string > > graph = 
    {
        { "a" , vector< string >{ "b", "c" } },
        { "b" , vector< string >{ "d" } },
        { "c" , vector< string >{ "e" } },
        { "d" , vector< string >{ "f" } },
        { "e" , vector< string >{ } },
        { "f" , vector< string >{ } }
    };

    dfsIter(graph, "a");
    cout << "\n";
    dfsRec(graph, "a");
    cout << "\n";
    bfs(graph, "a");
    return 0;
}