# c++

## 字符串
### memcpy
```c++
#include <iostream>  // from cout
#include <string.h>  // for memcpy
using namespace std;

int main()
{
	std::string info = "Welcome";
	const char * fromPtr = info.c_str();   // 长度比info多1, 因为最后有个0.
	int size = 10;
	char * bufferPtr = new char[1024];
	memcpy(bufferPtr, fromPtr, size);
	bufferPtr[size] = 0;
	std::cout << "info: " << bufferPtr << std::endl;
   return 0;
}
```

### 比较字符的前几个是否相等
```c++
#include <string.h>  // strncmp()
#include <iostream>
int main(){
	std::string s = "hello";
	// int strncmp ( const char * str1, const char * str2, size_t num );
	if (strncmp (s.c_str(), "hello2", 5) == 0) {
		std::cout << "shot" << std::endl;
	}
	
	if (strncmp (s.c_str(), "hll", 2) != 0) {
		std::cout << "not shot" << std::endl;
	}
    return 0;
}
```
### 接收char * 的函数不能转入string 
```c++
#include <iostream>
#include <string>
using namespace std;
void display(const char * chars) {
	std::cout << chars << std::endl;
}

int main()
{
	std::string str = "hello!";
	// error: cannot convert 'std::string {aka std::basic_string}'
	// display(str);  // error
	display(str.c_str());
    return 0;
}
```
###　istringstream例子
```c++
bool first_number_in_string(const string & s, double *n_ptr)
{
    istringstream is(s);
    while (!(is >> *n_ptr)) {
	is.clear();
	// Skip character.
	(void)is.get();
	if (is.eof()) return false;
    }
    return true;
}
```

### 判断字符串是否为空s.empty()
```c++
#include <iostream>
int main()
{
	std::string s = "";
	if (s.empty()) {
		std::cout << "s is empty" << std::endl;
	}
    return 0;
}
```
### 解析url中的参数
```c++
#include <iostream>
#include <vector>
#include <string>
#include <map>
// 解析url请求中的参数.

// display vector
template<typename T>
void display(std::vector<T> vec) {
	for (auto it = vec.begin(); it != vec.end(); it++){
		std::cout << *it << ", " << std::endl;
	}	
}

// display map
template<typename K, typename V>
void display(std::map<K, V> & map) {
	std::cout << "display template" << std::endl;
    for (auto it = map.begin(); it != map.end(); it++) {
        std::cout << it->first << " -> " << it->second << std::endl;
    }
}

void parse_url_params(const std::string url, std::map<std::string, std::string>* resultMapPtr) {
    // use = for the main signal of a pair
    std::string::size_type fromIndex = 0;  //
    std::string::size_type endIndex = 0;  // position of &
    std::string::size_type equalIndex = 0;  // position of =
    std::string::size_type size = url.size();

    fromIndex = url.find("?");
    if (fromIndex == std::string::npos) {
        return;
    }

    fromIndex += 1;  // skip ?
    equalIndex = url.find("=", fromIndex);

	bool isLastPair = false;
    std::string key;
    std::string value;
    while (equalIndex != std::string::npos) {
        endIndex = url.find("&", fromIndex);
        if (endIndex == std::string::npos) {
            // last pair
            endIndex = url.size();
			isLastPair = true;
        }
        key = url.substr(fromIndex, equalIndex - fromIndex);
        value = url.substr(equalIndex + 1, endIndex - equalIndex - 1);
        resultMapPtr->insert(std::make_pair(key, value));
    
		if (isLastPair) {
			break;
		}
        fromIndex = endIndex + 1;  // skip &
        equalIndex = url.find("=", fromIndex);
    }
    return;
}

int main()
{
    std::vector<std::string> urls{
        "http://www.runoob.com/try/runcode.php?filename=helloworld&type=cpp",
        "http://www.runoob.com/try/runcode.php?filename=",
        "http://www.runoob.com/try/runcode.php?=x",
        "http://www.runoob.com/try/runcode.php?x",
        "http://www.runoob.com/try/runcode.php?="
    };
    std::map<std::string, std::string> resultMap;
    for (auto it = urls.begin(); it != urls.end(); it++) {
		std::cout << "url: " << *it << std::endl;
        resultMap.clear();
        parse_url_params(*it, &resultMap);
        display(resultMap);
    }
    return 0;
}
```

## time
### 计算监控的时间差
```c++
#include <sys/time.h>  // timeval
#include <unistd.h>  // linux sleep()
#include <iostream>

// return millisecond 毫秒 
int timeElapse(const timeval startTime, const timeval endTime) {
    // struct timeval {
    //     time_t tv_sec; /* seconds */
    //     suseconds_t tv_usec; /* microseconds */
    // };

    // millisecond 毫秒
    // microsecond 微秒
    // 1 second = 10^3 millisecond
    // 1 millisecond = 10^3 microsecond
    struct timeval diffTime;
    if (endTime.tv_usec < startTime.tv_usec) {
        diffTime.tv_sec = endTime.tv_sec - startTime.tv_sec - 1;
        diffTime.tv_usec = 1000000 + endTime.tv_usec - startTime.tv_usec;
    } else {
        diffTime.tv_sec = endTime.tv_sec - startTime.tv_sec;
        diffTime.tv_usec = endTime.tv_usec - startTime.tv_usec;
    }

    int diffMilliseconds = diffTime.tv_sec * 1000 + diffTime.tv_usec / 1000;
    return diffMilliseconds;
}
    
int main() {
    struct timeval startTime;
    gettimeofday(&startTime, NULL);
	
    sleep(1);
	for (int i = 0; i <= 10000; i++) {
		for (int i = 0; i <= 10000; i++) {
		}
	}

    struct timeval endTime;
    gettimeofday(&endTime,NULL);

    std::cout << "startTime: " << startTime.tv_sec << "(s), " << startTime.tv_usec << "(us)" << std::endl;
    std::cout << "endTime: " << endTime.tv_sec << "(s), " << endTime.tv_usec << "(us)" << std::endl;
    std::cout << "elapse time: " << timeElapse(startTime, endTime) << "(ms)" << std::endl;
	
    return 0;
}
```

## 输出字符
###  copy + ostream_iterator 实现类似于python的join方法.
```
#include <iterator>  // std::ostream_iterator
#include <iostream>     // std::cout
#include <algorithm>    // std::copy
#include <vector>       // std::vector
int main()
{
    std::vector<float> numbers{1.1, 2.1, 3.1, 4.1, 5.1};
    std::cout << "numbers: ";
    std::copy(numbers.begin() + 1, 
        numbers.end(),
        std::ostream_iterator<float>(std::cout, ", "));

    std::cout << std::endl;
    return 0;
}

// 结果: 
// numbers: 2.1, 3.1, 4.1, 5.1, 
```
## 继承
```c++
#include <iostream>
using namespace std;

class A {
public:
	string x = "A.x";
	string z = "A.z";
};

class B : public A {
public:
	string x = "B.x";
	string y = "B.y";
};

int main()
{
	A a;
	B b;
   cout << "x in B: " << b.x
	   << ", y in B: " << b.y
	   << ", z in B: " << b.z;
   return 0;
}

// output:
// x in B: B.x, y in B: B.y, z in B: A.z
```

## 执行命令行
- 用system来执行
  可以使用 system()函数运行命令行命令，但是只能得到该命令行的 int 型返回值，并不能获得显示结果. 
  system函数在执行时，不会顺序执行接下来的代码，而会停留在system语句上，直到cmd指令执行完毕.
```
#include <stdlib.h>
#include <iostream>
int main(){

    int status_code;
    // status_code = system("ls > temp.txt");
    status_code = system("ls");
    std::cout << "status_code " << status_code << std::endl; 
    return 0;
}
```
- 通过管道来完成可以获得运行的结果, 首先用popen打开一个命令行的管道，然后通过fgets获得该管道传输的内容，也就是命令行运行的结果.
```c++
待补充
```
- 改进: 使用shared_ptr, pclose放里面
```c++
std::string execShellCmd(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::shared_ptr<FILE> pipe(popen(cmd, "r"), pclose);
    if (!pipe) throw std::runtime_error("popen() failed!");
    while (!feof(pipe.get())) {
        if (fgets(buffer.data(), 128, pipe.get()) != nullptr)
            result += buffer.data();
    }
    return result;
}
```

参考:
C++ 操作cmd并返回结果
http://blog.csdn.net/hguo11/article/details/51487644
C/C++ 程序中调用命令行命令并获取命令行输出结果
https://www.cnblogs.com/sylar5/p/6644870.html


## 算法
### merge sorted vector
```
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <queue>

#include <queue>
#include <vector>

using std::pair;
using std::make_pair;
using std::vector;

using namespace std;
void value_vectors(const vector< vector <int> * >& input_sorted_vectors, vector<int> &output_vector)
{
    typedef std::vector<int>::iterator iter;
    typedef std::pair<iter, iter> iter_pair;

    static auto less_than_lambda = [](const iter_pair& p1, const iter_pair& p2) -> bool { return *(p1.first) < *(p2.first); };

    priority_queue<iter_pair, std::vector<iter_pair>, decltype(less_than_lambda) > max_heap(less_than_lambda);

    size_t total_size(0);

    for (auto it = input_sorted_vectors.begin(); it != input_sorted_vectors.end(); ++it)
    {
        if (((*it)->size()) == 0) {
            continue;
        }
        max_heap.push( make_pair( (*it)->begin(), (*it)->end() ) );
        total_size += (*it)->size();
    }

    output_vector.resize(total_size);
    total_size = 0;
    iter_pair c_lead;
    while (max_heap.empty() != true)
    {
        c_lead = max_heap.top();
        max_heap.pop();
        output_vector[total_size++] = *(c_lead.first);
        c_lead.first++;
        if (c_lead.first != c_lead.second) max_heap.push(c_lead);
    }
}

int main() {
    vector<int> a{1,-2,-3,-4,-5,-7,-9,-10,-18};
    vector<int> b{};
    vector<int> c{-1,-7,-9, -10, -18};

    vector<vector<int> *> input_sorted_vectors{&a, &b, &c};
    vector<int> output_vector;
    value_vectors(input_sorted_vectors, output_vector);
    for (auto i: output_vector) {
        cout << i << ", ";
    }    
    return 0;
}
```
参考链接:
- https://stackoverflow.com/questions/9013485/c-how-to-merge-sorted-vectors-into-a-sorted-vector-pop-the-least-element-fro
  C++ How to merge sorted vectors into a sorted vector / pop the least element from all of them?
- K-way Merge in O(k n log k)
  https://coldfunction.com/mgen/p/3z  (最后多个vecotr merge的代码有问题)
- Merging K Sorted Arrays/Vectors Complexity
  https://stackoverflow.com/questions/39197996/merging-k-sorted-arrays-vectors-complexity





## 问题汇总

### cin 输入不合法后出现死循环
```c++
#include <iostream> 
int main(int argc, char** argv) {
    // char * a = "hello";
    std::string a = "hello";
    int b = 1;
    while(true) {
        std::cout << "===Please input a(string), b(int)=========" << std::endl;
        std::cin >> a >> b;
        std::cout << "you input is " << a << " " << b << std::endl;
    }
    
return 0;
}
```
在运行时, 如果输入不合法, 会一直死循环, 如:
```
===Please input a(string), b(int)=========
a 1
you input is a 1
===Please input a(string), b(int)=========
aa aa
you input is aa 0
===Please input a(string), b(int)=========
you input is aa 0
===Please input a(string), b(int)=========
you input is aa 0
===Please input a(string), b(int)=========
you input is aa 0
===Please input a(string), b(int)=========
you input is aa 0
===Please input a(string), b(int)=========
you input is aa 0
```

### cin时出现bug error
```c++
#include <iostream> 
int main(int argc, char** argv) {
    char * a = "hello";
    int b = 1;
    while(true) {
        std::cout << "===Please input a(char *), b(int)=========" << std::endl;
        std::cin >> a >> b;
        std::cout << "you input is " << a << " " << b << std::endl;
    }
    
return 0;
}
```
如下输入时会出现bus error
```
===Please input a(char *), b(int)=========
a 2
Bus error: 10
```

### map边迭代边erase出现问题
目的是把一个hash表种不同的key的value均匀地取出, 工程上可以用在不同召回源的均匀截断. 只是迭代器累加的地方不一样, 结果却不相同.
- 方法1, 正确
```c++
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{
    vector<int> a{1, 2};
    vector<int> b{11};
    vector<int> c{21, 22, 23, 24};
    
    map<int, vector<int>> hash;
    hash[1] = a;
    hash[2] = b;
    hash[3] = c;
  
    for (int idx = 0; idx < 100; idx++) {
        for (auto it = hash.begin(); it != hash.end();) {
            if (idx >= it->second.size()) {
                hash.erase(it++);
            } else {
                cout << it->second[idx] << ", ";
                it++;
            }
        }
    }
   return 0;
}

// result: 1, 11, 21, 2, 22, 23, 24, 
```
- 方法2, 不对, 多输出个2, 这个在mac会直接报Segmentation fault的错误.
```c++
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{
	vector<int> a{1, 2};
	vector<int> b{11};  // or b{}
	vector<int> c{21, 22, 23, 24};
	
	map<int, vector<int>> hash;
	hash[1] = a;
	hash[2] = b;
	hash[3] = c;
	
	for (int idx = 0; idx < 100; idx++) {
		for (auto it = hash.begin(); it != hash.end(); it++) {
			if (idx >= it->second.size()) {
				hash.erase(it);
			} else {
				cout << it->second[idx] << ", ";
			}
		}
	}
   return 0;
}

// result: 1, 11, 21, 2, 2, 22, 23, 24, 
```

参考:  C++ STL中map.erase(it++)用法原理解析
http://blog.csdn.net/liuzhi67/article/details/50950843


```c++
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{
	map<int, int> hash;
	hash[1] = 1;
	hash[2] = 2;
	hash[3] = 3;
	
	auto it = hash.begin();
	cout << it->second << endl; // 1
	hash.erase(it);
	cout << it->second << endl; // 1, 即使删除了, 仍然是有it仍然是有效的
	cout << (++it)->second << endl; // 2
   return 0;
}
```

## 知识点说明
### map []操作, 如果没有, 会初始化.
map中用[]进行读取时, 如果不存在相应的key, 则会先初始化一个, 对于value为std::vector类型时, 初始的vector为空.

```c++
#include <iostream>
#include <map>
#include <vector>
using namespace std;
class A {
	int a = 3;
};

int main()
{
	A a1;
	std::map<int, std::vector<A> > hash;
   cout << hash[1].size();  // 不会出错, 没有key为1, 当读取的时候会新建立, 值中的vector为空.
   return 0;
}
```

