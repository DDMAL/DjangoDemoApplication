# Developer Guidelines for the DDMAL

This document sets out the coding practices for the DDMAL. This includes the following areas:

1. Coding Styles and Practices
2. Version Control Usage
3. Issue Management and Tracking
4. Suggested Tools

## Coding Styles and Practices

Depending on the language and environment you find yourself, there are a number of "Best Practices" for coding we follow here. This section will introduce coding style guidelines.

### Writing Code

The Python style guide, "[PEP 8: Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)" sets out the best practices of writing Python code. Of particular note is the first point, "A Foolish Consistency is the Hobgoblin of Little Minds." That is, consistency should be a guide, not a set of laws. Adhering to a consistent style makes it easier for you and your co-workers to follow and understand your code, but consistency should always be balanced with clarity.

That said, there are some rules that you are expected to adhere to in writing your code, unless there is a *very* good reason. If you submit code to the projects that do not adhere to these guidelines, expect to be asked to justify your decision, or re-write your code.

The biggest exception to all of these guidelines is that, should you find yourself working on a file that does not adhere to these practices, that you follow the style in that file first and foremost.

### General Principles

1. [Spaces, not Tabs](http://legacy.python.org/dev/peps/pep-0008/#code-lay-out). This applies for *all* code you write. You must set your editor to insert four spaces per tab character.

2. [Avoid Extraeous White Space](http://legacy.python.org/dev/peps/pep-0008/#id17).

3. [Keep Comments Clear and Up-to-date](http://legacy.python.org/dev/peps/pep-0008/#id20).

4. [Follow Naming Conventions](http://legacy.python.org/dev/peps/pep-0008/#id20). For Python, variables and functions should be all lower-case and separated by underscores. Class names should be CapWords. Example:

```
class MyClass(object):
    def this_is_a_method(self, argument):
        my_name = "mud"
```

Since Python has no formal means of encapsulation (See the "[We are all consenting adults](http://codingstyleguide.com/style/39/we-are-all-consenting-adults)" rule), you should prefix internal helper methods with a single underscore. A double underscore can be used if you want the Python interpreter to apply name mangling, but you should [understand the consequences of this](http://legacy.python.org/dev/peps/pep-0008/#designing-for-inheritance).

For JavaScript, named functions and variables should be mixedCase. The exception to this is that if you are creating a function that operates like a class. "Private" methods should be prefixed by an underscore.

```
var MyObject = function(something)
{
    var defaults = {
        fullImage: null,
        previewImage: null
    };

    var init = function()
    {
        _doStuff();
    };

    var _doStuff = function()
    {
        /// stuff.
    };
}
```

### Style Guidelines and Examples

Taken from the [Cappuccino Style Guidelines](https://raw.githubusercontent.com/cappuccino/cappuccino/master/CONTRIBUTING.md). This will show some examples for bracketed languages (JavaScript/C++). Python examples are found in [PEP 8](http://legacy.python.org/dev/peps/pep-0008/).

### Trailing whitespace
Leave no trailing spaces or tabs at the end of a line (`trailing whitespace`), even if the line is empty and in an otherwise indented block.

### Indentation

Use spaces, not tabs. Tabs should only appear in files that require them for semantic meaning, like Makefiles. The indent size is 4 spaces.

##### Right:

    function main()
    {
        return 0;
    }

##### Wrong:

    function main()
    {
            return 0;
    }

    function main()
    {
\t  \t  return 0;
    }

---

A case label should be indented once from its switch statement. The case statement is indented once from its label. There should be one blank line between case + code blocks.

##### Right:

    switch (condition)
    {
        case fooCondition:
        case barCondition:
            i++;
            break;

        case bazCondition:
            i += 2;
            break;

        default:
            i--;
    }

##### Wrong:

    switch (condition) {
        case fooCondition:
        case barCondition:
            i++;
            break;
        case bazCondition:  i += 2;
                            break;
        default:
            i--;
    }

### Spacing

Do not place spaces around unary operators.

##### Right:

    i++

##### Wrong:

    i ++

---

Do place spaces around binary and ternary operators.

##### Right:

    y = m * x + b;
    f(a, b);
    c = a | b;
    return condition ? 1 : 0;

##### Wrong:

    y=m*x+b;
    f(a,b);
    c = a|b;
    return condition ? 1:0;

---

`if` statements with only one statement can omit braces UNLESS doing so makes the code unclear.

##### Right

    if (condition)
        doIt();

    if (condition)
        doIt();
    else
    {
        // something
        // something
        // something
    }

##### Acceptable

    if (condition)
    {
        doIt();
    }

##### Wrong

    // This will be an error
    if (condition)
        doIt();
        doSomethingElse();

    // unclear that this is just a one-liner.
    if (condition)
        myObject = {
            'foo': 'bar',
            'baz': 'bif'
        };

---

Place spaces between control statements and their parentheses.

##### Right:

    if (condition)
        doIt();

##### Wrong:

    if(condition)
        doIt();

---

Do not place spaces between a function and its parentheses, or between a parenthesis and its content.

##### Right:

    var init = function(a, b);

##### Wrong:

    var init = function (a, b);
    var init = function f( a, b );

---

### Line breaking

Each statement should get its own line.

##### Right:

    var x,
        y;
    x++;
    y++;

    if (condition)
        doIt();

##### Wrong:

    var x, y;
    x++; y++;
    if (condition) doIt();

There should be blank lines around bracketed code blocks and control structures, and a blank line after multiline var blocks.

##### Right:

    var x,
        y;

    x++;
    y++;

    if (condition)
        doIt();
    else
    {
        doSomethingElse();
        doMore();
    }

    return x;

##### Wrong:

    var x,
        y;
    x++;
    y++;
    if (condition)
        doIt();
    else
    {
        doSomethingElse();
        doMore();
    }
    return x;

### Braces

Every brace gets its own line, very simple to remember:

##### Right:

    int main()
    {
        //...
    }

    if (condition)
    {
        //...
    }
    else if (condition)
    {
        //...
    }

##### Wrong:

    int main() {
        ...
    }

    if (condition) {
        ...
    } else if (condition) {
        ...
    }

### Null, false and 0

In JavaScript, the null object value should be written as `null`.

Tests for `true/false`, `null/non-null`, and zero/non-zero should all be done without equality comparisons, except for cases when a value could be both 0 or `null` (or another "falsey" value). In this case, the comparison should be preceded by a comment explaining the distinction.

##### Right:

    if (condition)
        doIt();

    if (!ptr)
        return;

    if (!count)
        return;

    // object is an ID number, so 0 is OK, but null is not.
    if (object === null)
        return;

##### Wrong:

    if (condition == true)
        doIt();

    if (ptr == NULL)
        return;

    if (count == 0)
        return;

    if (object == null)
        return;

---

### Names

Use CamelCase. Capitalize the first letter of a class. Lower-case the first letter of a variable or function name. Fully capitalize acronyms.

##### Right:

    @implementation Data : //...
    @implementation HTMLDocument : //...

##### Wrong:

    @implementation data : //...
    @implementation HtmlDocument : //...

---

Multiple `var` declarations can be collapsed with commas, unless it makes it difficult to read.

##### Right:

    var index = 0,
        count = 5;

##### Wrong:

    var index = 0;
    var count = 5;

---

Variable declarations should be created as needed, rather than up front ("hoisted").

##### Right:

    - (BOOL)doSomething:(id)aFoo
    {
        var importantVariable = [aFoo message];

        if (!importantVariable)
            return;

        var index = [aFoo count];

        while (index--)
        {
            var innerVariable = [aFoo objectAtIndex:index];
            //do something;
        }
    }

##### Wrong:

    - (BOOL)doSomething:(id)aFoo
    {
        var importantVariable = [aFoo message],
            index = [aFoo count],
            innerVariable;

        if (!importantVariable)
            return;

        while (index--)
        {
            innerVariable = [aFoo objectAtIndex:index];
            //do something;
        }
    }

---

Use full words, except in the rare case where an abbreviation would be more canonical and easier to understand.

##### Right:

    var characterSize,
        length,
        tabIndex; // more canonical

##### Wrong:

    var charSize,
        len,
        tabulationIndex; // bizarre

---

Precede boolean values with words like "is" and "did".

##### Right:

    var isValid,
        didSendData;

##### Wrong:

    var valid,
        sentData;

    - (BOOL)editable;
    - (BOOL)receivedResponse;

---

Precede setters with the word "set". Use bare words for getters. Setter and getter names should match the names of the variables being set/gotten.

##### Right:

    setCount:(unsigned)aCount; // sets _count
    count; // returns _count

##### Wrong:

    getCount;

---

Use descriptive verbs in function names, and place desired types in comments.

##### Right:

    function convertToASCII(aString)

##### Wrong:

    function toASCII(str)

---

Use descriptive parameter names that are not abbreviated.

##### Right:

    convertString(aString, aFormat);
    appendSubviews(subviews, ordering = order);

##### Wrong:

    convertString(str,f);
    appendSubviews(s, ordering = flag);

---

*Python Only* Use formatting strings, not printf-like statements.

##### Right:

    "This will be {0} in the string".format("inserted")

##### Wrong:

    "This will be %s in the string" % "inserted"

---

## Version Control Usage

We use the Git version control system almost exclusively in the DDMAL.

If you are tasked with a new project, your first job is to establish a repository on the DDMAL GitHub page (http://github.com/DDMAL). You are expected to keep this repository up-to-date with your progress, with frequent commits. If your project is not ready for "prime time", then you should arrange a private repository.

Every project should have a "master" branch, where the most recent stable version of your code lives. This is flexible. If you are building something for the first time, you can publish to the master branch until your project becomes stable. When that happens, you should separate your work into two "mainline" branches, "master" and "develop". Do any development on the "develop" branch, and merge your changes into the master branch once they have been tested.

If a commit will break functioning code that others depend on (e.g., you want to work on a new feature that will break an existing feature) you are can work on a dedicated feature development branch. This branch should also be published on the shared page. You should be familiar with how to maintain separate branches and how to merge your work back into the mainline branches. While you should feel free to make as many branches as you need, you should also make sure that you keep track of the branches that you are working on, that you resolve them properly, and that you delete them when you are done with them.

### Commits

Almost all of your commits should be atomic. That is, they should address one, and only one, issue at a time. You should avoid "bulk" commits that address more than one issue. This makes it harder to trace back to a specific commit that introduced a bug or a change in behaviour in the code.

Notable exceptions to this are initial commits, code style cleanup commits, code re-organization commits. If you are starting a new project and have a lot of "boilerplate" code to write (e.g., writing all the models for a Django application, or defining the structure of a class), you may commit these in bulk.

You should avoid committing binary blobs of data, especially if they're a by-product of a building or running process. The following is a partial list of things you should never commit to a repository:

 * Any virtual environment ("virtualenv") folder.
 * `.DS_Store` files (if you're on a Mac)
 * `*.pyc` files. These are automatically generated when a Python script is run.
 * Database files, especially `.sqlite` files.
 * Any built or compiled files, e.g., a Solr `.war` file, a `.dylib` file, or a "Frameworks" folder (e.g., `mei.framework/`).

Binary blobs that you may commit include:

 * Images and image data
 * Small sound files (if they're part of an interface, and not part of a dataset)

To automatically exclude files from your commits, you should establish a `.gitignore` file for your project. If you create a new GitHub repository it gives you the option of adding a default `.gitignore` file.

### Commit messages

Adapted from the [Cappuccino Coding Guidelines](https://raw.githubusercontent.com/cappuccino/cappuccino/master/CONTRIBUTING.md).

Commit messages are crucial to communicating what you have done, and provide hints for all members of your team as they look back through your code. Our use of GitHub, and specifically the issue tracker in GitHub, allows for linking commits directly to issues so that we can maintain a full history of problems and solutions for our projects.

To help identify different types of commits, you should follow these commit message guidelines.

Commit messages should be in the following format:

    <type>: <summary>

    <body>

    <footer>

### Types

Allowed `type` values are:

* **New** — A new feature has been implemented
* **Fixed** — A bug has been fixed
* **Docs** — Documentation has been added or tweaked
* **Formatting** — Code has been reformatted to conform to style guidelines
* **Test** — Test cases have been added

### Message summary

The summary is one of the most important parts of the commit message, because that is what we see when scanning through a list of commits, and it is also what we use to generate change logs.

The summary should be a **concise** description of the commit, preferably 72 characters or less (so we can see the entire description in github), beginning with a lowercase letter and with a terminating period. It should describe only the core issue addressed by the commit. If you find that the summary needs to be very long, your commit is probably too big! Smaller commits are better.

For a `New` commit, the summary should answer the question, “What is new and where?” For a `Fixed` commit, the summary should answer the question, “What was fixed?”, for example “Window content view overlapped frame”. It should **not** answer the question, “What was done to fix it?” That belongs in the body.

Do **not** simply reference another issue or pull request by number in the summary. First of all, we want to know what was actually changed and why, which may not be fully explained in the referenced issue. Second, github will not create a link to the referenced issue in the commit summary.

### Message body

The details of the commit go in the body. Specifically, the body should include the motivation for the change for `New`, `Fixed` and `Task` types. For `Fixed` commits, you should also contrast behavior before the commit with behavior after the commit.

If the summary can completely express everything, there is no need for a message body.

### Message footer

If the commit closes an issue by fixing the bug, implementing a feature, or rendering it obsolete, or if it references an issue without closing it, that should be indicated in the message footer.

Issues closed by a commit should be listed on a separate line in the footer with an appropriate prefix:

- "Fixes" for `Fixed` commit types
- "Closes" for all other commit types

For example:

    Fixes #1234

or in the case of multiple issues, like this:

    Fixes #1234, #2345

Issues that a commit references without closing them should be listed on a separate line in the footer with the prefix "Refs", like this:

    Refs #1234

or in the case of multiple issues, like this:

    Refs #1234, #2345

### Examples

    New: Added a method to display kittens

    This method shows cute, cuddly kittens on the user's
    screen when they meow like a cat into their microphone.

    Closes #1234

***

    Fixed: Updated kitten display method

    Previously, the kitten display method did not
    differentiate between a 'meow' and a 'woof'.

    This commit adds another check to determine 
    whether the user is actually meowing.

    Fixes #4567

***

    Formatting: Removed extraneous whitespace

***

## Issue Management and Tracking

If you have a GitHub repository, you should maintain a list of all features, bugs, and support requests in the Issue tracker for that project. You should establish a taxonomy system for your issues that allow you to differentiate between different types of issues, e.g., between "server" and "client" issues, or between "bugs" and "feature requests".

### Documentation

The GitHub Wiki system is the most appropriate place for any documentation that you write. Please keep your documentation up to date.

## Suggested or Alternative Tools

The following tools are suggested for helping you write code and manage your projects. If you have a better solution, or are more comfortable with something else, please feel free to use it!

### Browsers

My own experience is that Google Chrome has the best developer tools and extension support. If you are working on web applications you may want to install the `JSON View` and `Dev HTTP Client` extensions.

Firefox and Safari are also good. I have not seen any acceptable examples of Internet Explorer in an application environment.

### Editors

Sublime Text is a very good development editor. You should use the `Package Control` extension, which provides a plugin management system for installing extensions.

TextMate is also very good. If you are an Emacs or Vim user, that is fine but be aware that you're on your own for support!

At the very least, your editor should support some form of linting or style-adherence. For example, the "[Emmett](http://docs.emmet.io)" plugin can provide some shortcuts for repetitive tasks ("boilerplate" code).

The "SublimeLinter" plugin is extremely useful for ensuring your code meets the PEP8 standards. If you use Sublime Text, you should install this package and the "SublimeLinter-flake8" package. You can also install other linters for JavaScript and other languages.

### Version Control

If you can use the `git` command line application effectively, that's great! However, some people may wish to use a GUI. SourceTree is a free application for managing your repositories. Personally, I use Tower but this is a paid application.

### Terminals

The built-in OSX terminal is fine, but a little limited in my opinion. I prefer iTerm 2.

### Shells

I use zsh, with a custom extension set (Oh My Zsh!).

### Documentation

The lab has a limited number of licenses for the Dash documentation viewer. Talk to me if you think you might benefit from having this installed.



