## base

```c#
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

// Declaration
string name = "Pail";
double salary = 9000.12;
int age;
age = 25;
int newAge = age;
var age1 = 25;
var newAge1 = age;


// Operators
int a = 5;
int b = 10;

int sum = a + b;
int diff = a - b;
int product = a * b;
int quotient = b / a;

string greeting = "Hello";
string name1 = "Paul";
string message = greeting + ", " + name1;
string upperName = name1.ToUpper();
string[] words = message.Split(' ');
string replacedMessage = message.Replace("Paul", "Tom");

Console.WriteLine("upperName:" + upperName);
Console.WriteLine("words:" + words);
Console.WriteLine("words 0:" + words[0]);
Console.WriteLine("words 1:" + words[1]);
Console.WriteLine("replacedMessage:" + replacedMessage);


// Logical operators
// AND    &&
// OR     ||
// NOT    !

// Comparison operators
// Equal to                   ==
// Not equal to               !=
// Greater than               >
// Less than                  <
// Greater than or equal to   >=
// Less than or equal to      <=

// Ternary operator
int nextMonth = DateTime.Now.Month == 12 ? 1 : DateTime.Now.Month + 1;

// Bitwise operators
// AND            &
// OR             |
// NOT            ~
// XOR            ^
// Left shift     <<
// Right shift    >>


// Data structures and collections
int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
List<int> numberList = new List<int>();
numberList.AddRange(numbers);
int firstNumber = numberList[0];
numberList.Remove(4);
Console.WriteLine("numberList:" + string.Join(",", numberList));
Console.WriteLine("numberList len:" + numberList.Count) ;


// Namespace declare
namespace ProductionApplication.CustomerManagement
{
    public class Customer { }
    public class DeliveryAddress { }
}

namespace ProductionApplication.AccountManagement
{
    public class Account { }
    public enum AccountType { }
}

namespace ProductionApplication.ProductStock
{
    public class ProductStock { }
    public interface IBaseProducte { }
}
// import
// using ProductionApplication.CustomerManagement;
// using ProductionApplication.AccountManagement;
// using ProductionApplication.ProductStock;

if (age > 10) { }
else if (age < 2) { }
else { }

switch (isDirectory)
{
    case true when myFile != null:
        break;
    case false:
        break;
    default:
        break;
}

string Weekend(DayOfWeek dayOfWeek)
{
    return dayOfWeek switch
    {
        DayOfWeek.Sunday => "Sunday",
        DayOfWeek.Saturday => "Saturday",
        _ => "It’s not weekend!"
    };
}

foreach (var item in collection) { }
foreach (var item in new[] { 1, 2, 3, 4, 5 }) { }
for (var i = 0; i < 10; i++) { }

while (myCondition) { }
do { }while(myCondition)

myLable:
// Code block
goto myLable;

tryAgain:
try
{
    var stream = new FileStream(filePath, FileMode.Open, FileAccess.Read);
    stream.Close();
    stream.Dispose();
}
catch
{
    Thread.Sleep(1_000);
    goto tryAgain;
}

IEnumerable<valueType> GetNumbers()
{
    yield return value1;
}


// 函数可以当作参数传递
ProcessNumbers(5, 3, Multiply);
static void ProcessNumbers(int a, int b, Func<int, int, int> operation) { }
static int Multiply(int x, int y) { }



// lambda expression
// (input parameters) => expression
Func<int, int> square = x => x * x;

Action<string> greet = name =>
{
    Console.WriteLine($"hello, {name}");
};

// 三个int表示传入类型和返回类型
Func<int, int, int> add = (x, y) => x + y;
int result = add(5, 10);

// 匿名
List<int> numbers = new List<int> { 2, 3, 4, 5, 6 };
var evenNumbers = numbers.Where(n => n % 2 == 0);
Func<int, int> doubleNumber = x => x * 2;
Console.WriteLine(doubleNumber(4));



```
