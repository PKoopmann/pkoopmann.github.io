import React, { useState, useEffect } from 'react';

// Load marked.js from CDN
// This script will be available globally as 'marked'
const markedScript = document.createElement('script');
markedScript.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
document.head.appendChild(markedScript);

// Define your Markdown content as constants
const markdownContent1 = `
# Welcome to Content 1!

This is a **sample** markdown file for the first section of your website.

## Features:
* Easy to read
* Supports **bold** and *italic* text
* Includes [links](https://www.google.com)
* Code blocks:
    \`\`\`javascript
    function greet(name) {
        return \`Hello, \${name}!\`;
    }
    console.log(greet('World'));
    \`\`\`

Here's a list:
1.  Item one
2.  Item two
    * Sub-item A
    * Sub-item B
3.  Item three

> This is a blockquote.
> It can span multiple lines.

---
A horizontal rule.
`;

const markdownContent2 = `
# Exploring Content 2

This section demonstrates another markdown page.

## Data Table Example:

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 2 Col 2 | Row 2 Col 3 |

## Image Example (Placeholder):

![Placeholder Image](https://placehold.co/600x400/FF5733/FFFFFF?text=Content+Image)

## More Text:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
`;

const markdownContent3 = `
# About Our Project

This page provides some information about the project.

## Our Mission

Our mission is to provide clear, concise, and accessible information to our users. We believe in the power of simplicity and efficiency.

## Contact Us

If you have any questions, feel free to reach out.

* **Email:** info@example.com
* **Phone:** +123 456 7890
* **Address:** 123 Main Street, Anytown, USA

## Technologies Used

* **React:** For building the user interface.
* **Tailwind CSS:** For styling and responsive design.
* **Marked.js:** For parsing Markdown content.
`;

// Main App component
export default function App() {
    const [currentPage, setCurrentPage] = useState('content1');
    const [parsedHtml, setParsedHtml] = useState('');

    // Function to parse Markdown and set HTML
    const parseAndSetHtml = (markdown) => {
        // Ensure marked.js is loaded before trying to use it
        if (window.marked) {
            setParsedHtml(window.marked.parse(markdown));
        } else {
            // Fallback or loading indicator if marked.js isn't ready
            setParsedHtml('<p>Loading Markdown parser...</p>');
            console.warn('marked.js not yet loaded.');
        }
    };

    // Effect to update content when currentPage changes
    useEffect(() => {
        let contentToParse = '';
        switch (currentPage) {
            case 'content1':
                contentToParse = markdownContent1;
                break;
            case 'content2':
                contentToParse = markdownContent2;
                break;
            case 'content3':
                contentToParse = markdownContent3;
                break;
            default:
                contentToParse = '# Page Not Found\n\nSorry, the requested page does not exist.';
        }
        parseAndSetHtml(contentToParse);
    }, [currentPage]); // Re-run when currentPage changes

    // Tailwind CSS classes for common elements
    const navLinkClasses = (page) =>
        `px-4 py-2 rounded-md text-sm font-medium transition-colors duration-200 ` +
        (currentPage === page
            ? 'bg-blue-600 text-white shadow-md'
            : 'text-gray-700 hover:bg-blue-100 hover:text-blue-700');

    return (
        <div className="min-h-screen bg-gray-100 font-sans text-gray-800 flex flex-col">
            {/* Tailwind CSS CDN */}
            <script src="https://cdn.tailwindcss.com"></script>
            {/* Header and Navigation */}
            <header className="bg-white shadow-sm py-4 px-6 md:px-8 lg:px-12">
                <nav className="container mx-auto flex flex-wrap justify-center md:justify-between items-center">
                    <h1 className="text-2xl font-bold text-blue-700 mb-4 md:mb-0">My Awesome Website</h1>
                    <div className="flex flex-wrap gap-3">
                        <button
                            className={navLinkClasses('content1')}
                            onClick={() => setCurrentPage('content1')}
                        >
                            Content 1
                        </button>
                        <button
                            className={navLinkClasses('content2')}
                            onClick={() => setCurrentPage('content2')}
                        >
                            Content 2
                        </button>
                        <button
                            className={navLinkClasses('content3')}
                            onClick={() => setCurrentPage('content3')}
                        >
                            About Project
                        </button>
                    </div>
                </nav>
            </header>

            {/* Main Content Area */}
            <main className="flex-grow container mx-auto p-6 md:p-8 lg:p-12">
                <div className="bg-white rounded-lg shadow-lg p-6 md:p-8 lg:p-10 prose max-w-none">
                    {/* Markdown content will be rendered here */}
                    <div dangerouslySetInnerHTML={{ __html: parsedHtml }} />
                </div>
            </main>

            {/* Footer */}
            <footer className="bg-gray-800 text-white py-4 px-6 md:px-8 lg:px-12 text-center text-sm">
                <div className="container mx-auto">
                    &copy; {new Date().getFullYear()} My Awesome Website. All rights reserved.
                </div>
            </footer>
        </div>
    );
}
