import json
import os

def load_db():
    if os.path.exists('modules.json'):
        with open('modules.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_db(db):
    with open('modules.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def main():
    db = load_db()
    
    dsa_module = {
        "id": 6,
        "name": "DSA",
        "short": "DSA",
        "color": "c-pink",
        "count": 55,
        "subs": [
            {
                "head": "Number System",
                "qs": [
                    {"q": "Write a Java program to check if a number is even or odd using bitwise.", "a": "<h4>Even or Odd (Bitwise)</h4><pre>public static boolean isEven(int n) {\n  return (n & 1) == 0;\n}</pre><em>Complexity:</em> <code>O(1)</code> time, <code>O(1)</code> space."},
                    {"q": "Write a Java program to reverse a number.", "a": "<h4>Reverse a Number</h4><pre>public static int reverse(int n) {\n  int rev = 0;\n  while(n != 0) {\n    rev = rev * 10 + n % 10;\n    n /= 10;\n  }\n  return rev;\n}</pre><em>Complexity:</em> <code>O(log10(N))</code> time, <code>O(1)</code> space."},
                    {"q": "Check if a number is a palindrome.", "a": "<h4>Number Palindrome</h4><pre>public static boolean isPalindrome(int n) {\n  if(n < 0) return false;\n  int temp = n, rev = 0;\n  while(temp != 0) {\n    rev = rev * 10 + temp % 10;\n    temp /= 10;\n  }\n  return n == rev;\n}</pre>"},
                    {"q": "Find the sum of digits of a number.", "a": "<h4>Sum of Digits</h4><pre>public static int sumDigits(int n) {\n  int sum = 0;\n  while(n != 0) {\n    sum += Math.abs(n % 10);\n    n /= 10;\n  }\n  return sum;\n}</pre>"},
                    {"q": "Check if a number is prime (optimized O(√n)).", "a": "<h4>Prime Check</h4><pre>public static boolean isPrime(int n) {\n  if(n <= 1) return false;\n  if(n <= 3) return true;\n  if(n % 2 == 0 || n % 3 == 0) return false;\n  for(int i = 5; i * i <= n; i += 6) {\n    if(n % i == 0 || n % (i + 2) == 0) return false;\n  }\n  return true;\n}</pre>"},
                    {"q": "Find the factorial of a number — iterative and recursive.", "a": "<h4>Factorial</h4><pre>// Iterative:\npublic static long factIter(int n) {\n  long res = 1;\n  for(int i=2; i<=n; i++) res *= i;\n  return res;\n}\n// Recursive:\npublic static long factRec(int n) {\n  return (n <= 1) ? 1 : n * factRec(n - 1);\n}</pre>"},
                    {"q": "Print Fibonacci series — iterative and recursive.", "a": "<h4>Fibonacci Series</h4><pre>// Iterative:\npublic static void fibIter(int n) {\n  int a=0, b=1;\n  for(int i=0; i&lt;n; i++) {\n    System.out.print(a + \" \");\n    int next = a + b;\n    a = b; b = next;\n  }\n}</pre>"},
                    {"q": "Check if a number is an Armstrong number.", "a": "<h4>Armstrong Number</h4><pre>public static boolean isArmstrong(int n) {\n  int temp = n, sum = 0, digits = String.valueOf(n).length();\n  while(temp != 0) {\n    sum += Math.pow(temp % 10, digits);\n    temp /= 10;\n  }\n  return sum == n;\n}</pre>"},
                    {"q": "Find GCD of two numbers using Euclidean algorithm.", "a": "<h4>Greatest Common Divisor (GCD)</h4><pre>public static int gcd(int a, int b) {\n  return (b == 0) ? a : gcd(b, a % b);\n}</pre>"},
                    {"q": "Find LCM using GCD.", "a": "<h4>Lowest Common Multiple (LCM)</h4><pre>public static int lcm(int a, int b) {\n  return (a * b) / gcd(a, b);\n}</pre>"},
                    {"q": "Convert decimal to binary (manual method).", "a": "<h4>Decimal to Binary</h4><pre>public static String decToBin(int n) {\n  StringBuilder sb = new StringBuilder();\n  while(n > 0) {\n    sb.append(n % 2);\n    n /= 2;\n  }\n  return sb.reverse().toString();\n}</pre>"},
                    {"q": "Convert binary to decimal.", "a": "<h4>Binary to Decimal</h4><pre>public static int binToDec(String bin) {\n  int dec = 0, power = 0;\n  for(int i=bin.length()-1; i>=0; i--) {\n    if(bin.charAt(i) == '1') {\n      dec += Math.pow(2, power);\n    }\n    power++;\n  }\n  return dec;\n}</pre>"},
                    {"q": "Count the number of set bits (1s) in binary representation.", "a": "<h4>Set Bits Count</h4><pre>public static int countSetBits(int n) {\n  int count = 0;\n  while(n > 0) {\n    n = n & (n - 1); // Brian Kernighan's Algorithm\n    count++;\n  }\n  return count;\n}</pre>"},
                    {"q": "Swap two numbers without a temp variable.", "a": "<h4>Swap without Temp</h4><pre>// Using XOR:\na = a ^ b;\nb = a ^ b;\na = a ^ b;</pre>"},
                    {"q": "Check if a number is a power of 2 using bitwise.", "a": "<h4>Power of 2 Check</h4><pre>public static boolean isPowerOfTwo(int n) {\n  return n > 0 && (n & (n - 1)) == 0;\n}</pre>"},
                    {"q": "Find all prime numbers up to N (Sieve of Eratosthenes).", "a": "<h4>Sieve of Eratosthenes</h4><pre>public static void sieve(int n) {\n  boolean[] prime = new boolean[n+1];\n  Arrays.fill(prime, true);\n  for(int p=2; p*p<=n; p++) {\n    if(prime[p]) {\n      for(int i=p*p; i<=n; i+=p) prime[i] = false;\n    }\n  }\n  for(int i=2; i<=n; i++) if(prime[i]) System.out.print(i + \" \");\n}</pre>"},
                    {"q": "Check if a number is a perfect number.", "a": "<h4>Perfect Number</h4><pre>public static boolean isPerfect(int n) {\n  int sum = 1;\n  for(int i=2; i*i<=n; i++) {\n    if(n % i == 0) {\n      sum += i;\n      if(i * i != n) sum += n / i;\n    }\n  }\n  return sum == n && n != 1;\n}</pre>"},
                    {"q": "Find the largest of three numbers without if-else.", "a": "<h4>Largest of Three (Ternary)</h4><pre>int largest = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);</pre>"},
                    {"q": "Print a multiplication table for N.", "a": "<h4>Multiplication Table</h4><pre>for(int i=1; i<=10; i++) {\n  System.out.printf(\"%d x %d = %d\\n\", n, i, n * i);\n}</pre>"},
                    {"q": "Reverse digits and check for integer overflow.", "a": "<h4>Safe Reverse with Overflow Check</h4><pre>public static int reverseSafe(int n) {\n  int rev = 0;\n  while(n != 0) {\n    int tail = n % 10;\n    int newRev = rev * 10 + tail;\n    if((newRev - tail) / 10 != rev) return 0; // Overflow\n    rev = newRev;\n    n /= 10;\n  }\n  return rev;\n}</pre>"}
                ]
            },
            {
                "head": "Arrays",
                "qs": [
                    {"q": "Find the maximum and minimum element in an array.", "a": "<h4>Max & Min</h4><pre>int max = arr[0], min = arr[0];\nfor(int val : arr) {\n  if(val > max) max = val;\n  if(val < min) min = val;\n}</pre>"},
                    {"q": "Reverse an array in-place.", "a": "<h4>In-Place Reverse</h4><pre>int left = 0, right = arr.length-1;\nwhile(left < right) {\n  int temp = arr[left];\n  arr[left++] = arr[right];\n  arr[right--] = temp;\n}</pre>"},
                    {"q": "Find the second largest element.", "a": "<h4>Second Largest</h4><pre>int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE;\nfor(int val : arr) {\n  if(val > max1) { max2 = max1; max1 = val; }\n  else if(val > max2 && val != max1) { max2 = val; }\n}</pre>"},
                    {"q": "Remove duplicates from a sorted array in-place.", "a": "<h4>Remove Duplicates</h4><pre>public static int removeDuplicates(int[] arr) {\n  int index = 1;\n  for(int i=1; i&lt;arr.length; i++) {\n    if(arr[i] != arr[i-1]) arr[index++] = arr[i];\n  }\n  return index;\n}</pre>"},
                    {"q": "Find the sum and average of array elements.", "a": "<h4>Sum & Average</h4><pre>double sum = 0;\nfor(int val : arr) sum += val;\ndouble avg = sum / arr.length;</pre>"},
                    {"q": "Rotate an array by k positions (left and right).", "a": "<h4>Array Rotation (O(N) Time, O(1) Space)</h4><pre>// Reverse approach:\n// To rotate right by k: reverse(0, n-1) -> reverse(0, k-1) -> reverse(k, n-1)</pre>"},
                    {"q": "Check if an array is sorted in ascending order.", "a": "<h4>Check Sorted</h4><pre>boolean isSorted = true;\nfor(int i=1; i&lt;arr.length; i++) {\n  if(arr[i] < arr[i-1]) { isSorted = false; break; }\n}</pre>"},
                    {"q": "Merge two sorted arrays without extra space.", "a": "<h4>Merge without Extra Space</h4><pre>// Gap Algorithm / Shell sort method</pre>"},
                    {"q": "Find the missing number in 1 to N (formula and XOR approach).", "a": "<h4>Find Missing Number</h4><pre>// XOR Approach:\nint xorAll = 0, xorArr = 0;\nfor(int i=1; i<=n; i++) xorAll ^= i;\nfor(int val : arr) xorArr ^= val;\nint missing = xorAll ^ xorArr;</pre>"},
                    {"q": "Find the duplicate element in an array of 1 to N.", "a": "<h4>Find Duplicate (Floyd's Cycle Finding)</h4><pre>int slow = arr[0], fast = arr[0];\ndo { slow = arr[slow]; fast = arr[arr[fast]]; } while (slow != fast);\nfast = arr[0];\nwhile(slow != fast) { slow = arr[slow]; fast = arr[fast]; }\nreturn slow;</pre>"},
                    {"q": "Two Sum — find a pair that adds up to a target.", "a": "<h4>Two Sum</h4><pre>public static int[] twoSum(int[] arr, int target) {\n  Map<Integer, Integer> map = new HashMap<>();\n  for(int i=0; i&lt;arr.length; i++) {\n    int complement = target - arr[i];\n    if(map.containsKey(complement)) return new int[]{map.get(complement), i};\n    map.put(arr[i], i);\n  }\n  return new int[]{-1, -1};\n}</pre>"},
                    {"q": "Maximum Subarray Sum — Kadane's Algorithm.", "a": "<h4>Kadane's Algorithm</h4><pre>public static int maxSubArray(int[] arr) {\n  int maxSoFar = arr[0], currentMax = arr[0];\n  for(int i=1; i&lt;arr.length; i++) {\n    currentMax = Math.max(arr[i], currentMax + arr[i]);\n    maxSoFar = Math.max(maxSoFar, currentMax);\n  }\n  return maxSoFar;\n}</pre>"},
                    {"q": "Move all zeros to the end maintaining relative order.", "a": "<h4>Move Zeros</h4><pre>int index = 0;\nfor(int val : arr) if(val != 0) arr[index++] = val;\nwhile(index < arr.length) arr[index++] = 0;</pre>"},
                    {"q": "Find the intersection of two arrays.", "a": "<h4>Intersection of Arrays</h4><pre>// Put array A in a Set, filter array B elements present in the Set.</pre>"},
                    {"q": "Find the union of two arrays.", "a": "<h4>Union of Arrays</h4><pre>// Add all elements of both arrays to a single HashSet.</pre>"},
                    {"q": "Implement binary search iteratively and recursively.", "a": "<h4>Binary Search</h4><pre>public static int binarySearch(int[] arr, int target) {\n  int low = 0, high = arr.length - 1;\n  while(low <= high) {\n    int mid = low + (high - low)/2;\n    if(arr[mid] == target) return mid;\n    if(arr[mid] < target) low = mid + 1;\n    else high = mid - 1;\n  }\n  return -1;\n}</pre>"},
                    {"q": "Implement bubble sort — show the optimization.", "a": "<h4>Optimized Bubble Sort</h4><pre>for(int i=0; i&lt;n-1; i++) {\n  boolean swapped = false;\n  for(int j=0; j&lt;n-i-1; j++) {\n    if(arr[j] > arr[j+1]) {\n      swap(arr, j, j+1); swapped = true;\n    }\n  }\n  if(!swapped) break;\n}</pre>"},
                    {"q": "Implement selection sort.", "a": "<h4>Selection Sort</h4><pre>for(int i=0; i&lt;n-1; i++) {\n  int minIdx = i;\n  for(int j=i+1; j&lt;n; j++) {\n    if(arr[j] < arr[minIdx]) minIdx = j;\n  }\n  swap(arr, i, minIdx);\n}</pre>"},
                    {"q": "Implement insertion sort.", "a": "<h4>Insertion Sort</h4><pre>for(int i=1; i&lt;n; i++) {\n  int key = arr[i], j = i - 1;\n  while(j >= 0 && arr[j] > key) {\n    arr[j+1] = arr[j]; j--;\n  }\n  arr[j+1] = key;\n}</pre>"},
                    {"q": "Rearrange positive and negative numbers alternately.", "a": "<h4>Alternate Rearrange</h4><pre>// Two pointer approach matching parity indexes.</pre>"},
                    {"q": "Find the majority element (appears more than n/2 times).", "a": "<h4>Boyer-Moore Voting Algorithm</h4><pre>int candidate = arr[0], count = 1;\nfor(int i=1; i&lt;arr.length; i++) {\n  if(count == 0) { candidate = arr[i]; count = 1; }\n  else if(arr[i] == candidate) count++;\n  else count--;\n}\nreturn candidate;</pre>"},
                    {"q": "Find the equilibrium index of an array.", "a": "<h4>Equilibrium Index</h4><pre>// Compute totalSum. Traverse array, keeping track of leftSum.\n// RightSum = totalSum - leftSum - arr[i]. If leftSum == rightSum, return i.</pre>"},
                    {"q": "Count inversions in an array.", "a": "<h4>Count Inversions</h4><pre>// Modify Merge Sort logic. When merging, if left element > right element, all remaining left elements are inverted.</pre>"},
                    {"q": "Find the subarray with a given sum (sliding window).", "a": "<h4>Sliding Window Sum</h4><pre>// Maintain window sum. If sum > target, contract from left. If sum == target, return bounds.</pre>"},
                    {"q": "Find the longest increasing subsequence length (basic DP).", "a": "<h4>Longest Increasing Subsequence (LIS)</h4><pre>public static int lis(int[] arr) {\n  int[] dp = new int[arr.length];\n  Arrays.fill(dp, 1);\n  int max = 1;\n  for(int i=1; i&lt;arr.length; i++) {\n    for(int j=0; j&lt;i; j++) {\n      if(arr[i] > arr[j]) dp[i] = Math.max(dp[i], dp[j] + 1);\n    }\n    max = Math.max(max, dp[i]);\n  }\n  return max;\n}</pre>"}
                ]
            },
            {
                "head": "Strings",
                "qs": [
                    {"q": "Reverse a string in Java (without built-in reverse).", "a": "<h4>Reverse String</h4><pre>public static String reverse(String s) {\n  char[] chars = s.toCharArray();\n  int l = 0, r = chars.length-1;\n  while(l < r) {\n    char temp = chars[l];\n    chars[l++] = chars[r];\n    chars[r--] = temp;\n  }\n  return new String(chars);\n}</pre>"},
                    {"q": "Check if a string is a palindrome.", "a": "<h4>String Palindrome</h4><pre>public static boolean isPalindrome(String s) {\n  int l = 0, r = s.length()-1;\n  while(l < r) {\n    if(s.charAt(l++) != s.charAt(r--)) return false;\n  }\n  return true;\n}</pre>"},
                    {"q": "Count vowels and consonants in a string.", "a": "<h4>Vowels and Consonants</h4><pre>// Loop over string, checking character categories.</pre>"},
                    {"q": "Remove all whitespace from a string.", "a": "<h4>Remove Whitespace</h4><pre>s = s.replaceAll(\"\\\\s\", \"\");</pre>"},
                    {"q": "Check if two strings are anagrams.", "a": "<h4>Anagram Check</h4><pre>public static boolean isAnagram(String s1, String s2) {\n  if(s1.length() != s2.length()) return false;\n  int[] counts = new int[256];\n  for(int i=0; i&lt;s1.length(); i++) {\n    counts[s1.charAt(i)]++;\n    counts[s2.charAt(i)]--;\n  }\n  for(int c : counts) if(c != 0) return false;\n  return true;\n}</pre>"},
                    {"q": "Find the frequency of each character in a string.", "a": "<h4>Character Frequency</h4><pre>// Use a Map or simple frequency integer array for ASCII values.</pre>"},
                    {"q": "Find the first non-repeating character.", "a": "<h4>First Non-Repeating Character</h4><pre>// Count frequencies in first pass, lookup first character with count == 1 in second pass.</pre>"},
                    {"q": "Check if a string contains only digits.", "a": "<h4>Digits Check</h4><pre>public static boolean onlyDigits(String s) {\n  return s.matches(\"\\\\d+\");\n}</pre>"},
                    {"q": "Find the longest common prefix among an array of strings.", "a": "<h4>Longest Common Prefix</h4><pre>public static String lcp(String[] strs) {\n  if(strs.length == 0) return \"\";\n  String prefix = strs[0];\n  for(int i=1; i&lt;strs.length; i++) {\n    while(strs[i].indexOf(prefix) != 0) {\n      prefix = prefix.substring(0, prefix.length() - 1);\n    }\n  }\n  return prefix;\n}</pre>"},
                    {"q": "Count occurrences of a substring in a string.", "a": "<h4>Substring Occurrences</h4><pre>// Use indexOf repeatedly in a loop, incrementing indices.</pre>"},
                    {"q": "Check if one string is a rotation of another.", "a": "<h4>Rotation Check</h4><pre>public static boolean isRotation(String s1, String s2) {\n  return s1.length() == s2.length() && (s1 + s1).contains(s2);\n}</pre>"},
                    {"q": "Compress a string using run-length encoding (e.g., aaabbc → a3b2c1).", "a": "<h4>Run Length Compression</h4><pre>// Traverse string tracking current run counts. Append results to StringBuilder.</pre>"},
                    {"q": "Find the longest palindromic substring.", "a": "<h4>Longest Palindromic Substring</h4><pre>// Expand around centers: check odd and even length centers for palindromes.</pre>"},
                    {"q": "Find the longest substring without repeating characters.", "a": "<h4>Longest Substring (Sliding Window Map)</h4><pre>public static int lengthOfLongestSubstring(String s) {\n  Map<Character, Integer> map = new HashMap<>();\n  int max = 0, left = 0;\n  for(int i=0; i&lt;s.length(); i++) {\n    if(map.containsKey(s.charAt(i))) left = Math.max(left, map.get(s.charAt(i)) + 1);\n    map.put(s.charAt(i), i);\n    max = Math.max(max, i - left + 1);\n  }\n  return max;\n}</pre>"},
                    {"q": "Reverse words in a sentence.", "a": "<h4>Reverse Words</h4><pre>public static String reverseWords(String s) {\n  String[] words = s.trim().split(\"\\\\s+\");\n  Collections.reverse(Arrays.asList(words));\n  return String.join(\" \", words);\n}</pre>"},
                    {"q": "Remove duplicate characters from a string.", "a": "<h4>Remove Duplicates</h4><pre>// Add all characters to a LinkedHashSet to preserve order, build output string.</pre>"},
                    {"q": "Check if a string is a valid integer.", "a": "<h4>Valid Integer Check</h4><pre>// Match string against negative/positive number regex: ^[-+]?\\d+$</pre>"},
                    {"q": "Convert a string to an integer without parseInt (atoi).", "a": "<h4>Custom String to Integer</h4><pre>// Parse character digit values sequentially, updating result variables.</pre>"},
                    {"q": "Find all permutations of a string.", "a": "<h4>String Permutations</h4><pre>// Backtracking algorithm swapping indices.</pre>"},
                    {"q": "Check if two strings are equal ignoring case without equalsIgnoreCase.", "a": "<h4>Custom Case-Insensitive Compare</h4><pre>// Convert characters to lower case manual checks character by character.</pre>"}
                ]
            }
        ]
    }
    
    # Check if exists, replace or append
    idx = -1
    for i, m in enumerate(db):
        if m['id'] == 6:
            idx = i
            break
    if idx != -1:
        db[idx] = dsa_module
    else:
        db.append(dsa_module)
        
    save_db(db)
    print("DSA data populated successfully.")

if __name__ == '__main__':
    main()
