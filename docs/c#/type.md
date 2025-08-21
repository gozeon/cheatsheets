```c#
using System;
using System.Collections;
using System.Collections.Concurrent;
using System.Collections.Immutable;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using static System.Net.Mime.MediaTypeNames;

// Encoding
string filePath = @"C:\Users\admin\source\repos\ConsoleApp1\ConsoleApp1\TextFile1.txt";
Encoding gb2312 = Encoding.Unicode;

try
{
    using StreamReader reader = new StreamReader(filePath, gb2312);
    string content = reader.ReadToEnd();
    Console.WriteLine(content);
}catch(Exception ex)
{
    Console.WriteLine("An error:" + ex.Message);
}

// string
string hello = "hello,";
string world = "World!";
string combined = hello + world;
Console.WriteLine(combined);
Console.WriteLine(combined.Length);
Console.WriteLine(combined[4]);
Console.WriteLine(combined.Substring(7, 5));
Console.WriteLine(combined.IndexOf("World"));
Console.WriteLine(combined.Replace("World", "Universe"));
Console.WriteLine("apple,banana,cherry".Split(","));
Console.WriteLine("  trim   ".Trim());
Console.WriteLine(hello.ToUpper());
Console.WriteLine(hello.ToLower());
Console.WriteLine(hello == "hello,");
Console.WriteLine("42".PadLeft(5, '0'));

Console.WriteLine($"hello, {world}");
Console.WriteLine(string.Format("hello, {0}", world));

string[] words = { hello, world };
Console.WriteLine(string.Join(" ", words));


// Regular expressions
var urlPattern = @"https?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?";
var emailPattern = @"^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$";
var emails = new[] { "test@example.com", "invalid-email@", "sample@domain.org" };
foreach (var email in emails)
{
    Console.WriteLine($"{email} is {(Regex.IsMatch(email, emailPattern))}");
}

var numberPattern = @"\d+";
var textWithNumbers = "I have 5 apples and 10 oranges.";
var matches = Regex.Matches(textWithNumbers, numberPattern);
foreach (Match match in matches)
{
    Console.WriteLine(match.Value);
}

var whitespacePattern = @"\s+";
var spacedText = "This    has   irregular     spaces.";
var cleanedText = Regex.Replace(spacedText, whitespacePattern, " ");
Console.WriteLine($"Cleaned: { cleanedText}");


// Escaping and unescaping
string originalUrlString = "This is a query with special chars like & and spaces!";
string escapedUrlString = WebUtility.UrlEncode(originalUrlString);
Console.WriteLine($"Escaped URL: {escapedUrlString}");
string unescapedUrlString = WebUtility.UrlDecode(escapedUrlString);
Console.WriteLine("unescaping URL: " + unescapedUrlString);

// enum
// enum Colors { Red = 1, Green = 2, Blue = 4 };

// tuple
var person = (Name: "John", Age: 30);
Console.WriteLine(person.Name);

// null
Nullable<int> anotherNullableInt = null;
int? num = null;
if (num.HasValue)
{
    Console.WriteLine($"Value is: {num.Value}");
}
int b = num ?? 2;

// Datetime
DateTime time = new DateTime(0);
Console.WriteLine(time); // 0001-01-01 00:00:00
DateTime someDateTime = new DateTime(2023, 8, 11);
long unixTimestamp = (someDateTime.Ticks - new DateTime(1970, 1, 1).Ticks) / TimeSpan.TicksPerSecond;
Console.WriteLine(unixTimestamp); // 1691712000
DateTime originalDate = new DateTime(1970, 1, 1).AddSeconds(unixTimestamp);
Console.WriteLine(originalDate); // 2023-08-11 00:00:00
DateTime aestDateTime = new DateTime(2023, 8, 11, 14, 0, 0,DateTimeKind.Unspecified);
Console.WriteLine(aestDateTime);
string dateString = "2023-08-12 15:30:00";
DateTime dateTime = DateTime.Parse(dateString);
Console.WriteLine(dateTime);

// Collection
var arrayList = new ArrayList { "apple", 42, true };
Console.WriteLine($"ArrayList: {string.Join(", ", arrayList.Cast<object>())}");

var hashTable = new Hashtable
{
    {"key", "value" },
    {"a", 42 }
};
Console.WriteLine($"key={hashTable["key"]},a={hashTable["a"]}");

var queue = new Queue();
queue.Enqueue("apple");
queue.Enqueue(42);
Console.WriteLine($"Queue (after two enqueues): {string.Join(", ", queue.Cast<object>())}");
var dequeuedValue = queue.Dequeue();
Console.WriteLine($"Dequeued from Queue: {dequeuedValue}");

var stack = new Stack();
stack.Push("apple");
stack.Push(42);
Console.WriteLine($"Stack (after two pushes): {string.Join(", ", stack.Cast<object>())}");
var poppedValue = stack.Pop();
Console.WriteLine($"Popped from Stack: {poppedValue}");

var bitArray = new BitArray(new[] { true, false, true });
foreach (bool bit in bitArray)
{
    Console.Write(bit + " ");
}


// with type
var dictionary = new Dictionary<string, string>
{
    {"key1", "value1" },
    {"key2", "value2" }
};
Console.WriteLine($"Dictionary: {string.Join(", ", dictionary)}");

var queue1 = new Queue<int>();
queue1.Enqueue(1);
queue1.Enqueue(2);
Console.WriteLine($"Queue1 (after two enqueues): {string.Join(", ", queue1)}");
int dequeuedValue1 = queue1.Dequeue();
Console.WriteLine($"Dequeued from Queue1: {dequeuedValue1}");

var stack1 = new Stack<int>();
stack1.Push(3);
stack1.Push(4);
Console.WriteLine($"Stack1 (after two pushes): {string.Join(", ", stack1)}");
int poppedValue1 = stack1.Pop();
Console.WriteLine($"Popped from Stack1: {poppedValue1}");

var hashSet = new HashSet<int> { 5, 6, 6 };
Console.WriteLine($"HashSet: {string.Join(", ", hashSet)}");

var linkedList = new LinkedList<string>();
linkedList.AddLast("firstElement");
linkedList.AddLast("secondElement");
Console.WriteLine($"LinkedList: {string.Join(", ", linkedList)}");


// auto sort
var sortedSet = new SortedSet<int> { 8, 7, 9 };
Console.WriteLine($"SortedSet: {string.Join(", ", sortedSet)}");

var sortedList = new SortedList<string, string>
{
    {"b", "valueb" },
    {"a", "valuea" },
};
Console.WriteLine($"SortedList: {string.Join(", ", sortedList)}");

var sortedDictionary = new SortedDictionary<string, string>
{
    {"b", "valueb" },
    {"a", "valuea" },
};
Console.WriteLine($"SortedDictionary: {string.Join(", ",sortedDictionary)}");

// concurrent
var concurrentDictionary = new ConcurrentDictionary<string,string>();
concurrentDictionary.TryAdd("b", "valueb");
concurrentDictionary.TryAdd("a", "valuea");
Console.WriteLine($"ConcurrentDictionary: {string.Join(", ", concurrentDictionary)}");

var concurrentQueue = new ConcurrentQueue<int>();
concurrentQueue.Enqueue(1);
concurrentQueue.Enqueue(2);
concurrentQueue.TryDequeue(out int queueResult);
Console.WriteLine($"Dequeued from ConcurrentQueue: { queueResult}");

var concurrentStack = new ConcurrentStack<int>();
concurrentStack.Push(3);
concurrentStack.Push(4);
concurrentStack.TryPop(out int stackResult);
Console.WriteLine($"Popped from ConcurrentStack: {stackResult}");

var concurrentBag = new ConcurrentBag<int>();
concurrentBag.Add(5);
concurrentBag.Add(6);
concurrentBag.TryTake(out int bagResult);
Console.WriteLine($"Taken from ConcurrentBag: {bagResult}");

var blockingCollection = new BlockingCollection<int>(5);
blockingCollection.Add(7);
blockingCollection.Add(8);
Console.WriteLine($"BlockingCollection (after two additions): { string.Join(", ", blockingCollection)}");
int blockingResult = blockingCollection.Take();
Console.WriteLine($"Taken from BlockingCollection: { blockingResult}");

// immutable
ImmutableArray<int> immutableArray = ImmutableArray.Create(1, 2, 3, 4);
Console.WriteLine($"ImmutableArray: {string.Join(", ",immutableArray)}");

ImmutableList<int> immutableList = ImmutableList.Create(5, 6,7, 8);
Console.WriteLine($"ImmutableList: {string.Join(", ", immutableList)}");

var builder = ImmutableDictionary.CreateBuilder<string,string>();
builder.Add("b", "valueb");
builder.Add("a", "valuea");
ImmutableDictionary<string, string> immutableDictionary = builder.ToImmutable();
Console.WriteLine($"ImmutableDictionary: {string.Join(", ", immutableDictionary)}");

ImmutableHashSet<int> immutableHashSet = ImmutableHashSet.Create(9, 10, 11);
Console.WriteLine($"ImmutableHashSet: {string.Join(", ", immutableHashSet)}");

ImmutableQueue<int> immutableQueue = ImmutableQueue.Create(12, 13, 14);
immutableQueue = immutableQueue.Enqueue(15);
Console.WriteLine($"ImmutableQueue (after Enqueue): { string.Join(", ", immutableQueue)}");
var dequeuedValue2 = immutableQueue.Dequeue(); // dequeuedValue2 is new queue
Console.WriteLine($"Dequeued value from ImmutableQueue: {dequeuedValue2.Peek()}, is empty: {dequeuedValue2.IsEmpty}");

ImmutableStack<int> immutableStack = ImmutableStack.Create(16,17, 18);
immutableStack = immutableStack.Push(19);
Console.WriteLine($"ImmutableStack (after Push): {string.Join(", ", immutableStack)}");
var poppedValue2 = immutableStack.Pop();// poppedValue2 is new Stack
Console.WriteLine($"Popped value from ImmutableStack: { poppedValue2.Peek()}, is empty: { poppedValue2.IsEmpty}");

```
