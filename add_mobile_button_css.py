#!/usr/bin/env python3
"""
Add mobile button optimizations to admin-pusat HTML files
"""

files_to_update = [
    '/home/fritz/Fritz Kevin Manurung/Work/Magang/kemnaker/superadmin/admin-pusat/create.html',
    '/home/fritz/Fritz Kevin Manurung/Work/Magang/kemnaker/superadmin/admin-pusat/edit.html',
    '/home/fritz/Fritz Kevin Manurung/Work/Magang/kemnaker/superadmin/admin-pusat/show.html',
]

mobile_css = '''
            /* Mobile button optimizations */
            button, a.flex {
                font-size: 0.813rem !important; /* 13px */
                padding-top: 0.5rem !important; /* py-2 */
                padding-bottom: 0.5rem !important;
                padding-left: 0.75rem !important; /* px-3 */
                padding-right: 0.75rem !important;
            }

            button svg, a svg {
                width: 1rem !important; /* w-4 */
                height: 1rem !important; /* h-4 */
                margin-right: 0.375rem !important; /* mr-1.5 */
            }

            select, input[type="text"], input[type="search"] {
                font-size: 0.813rem !important;
                padding: 0.5rem 0.75rem !important;
            }
        }'''

def add_mobile_css(content):
    """Add mobile CSS before the closing of @media (max-width: 640px)"""
    import re
    
    # Find the @media (max-width: 640px) section and add mobile CSS before its closing brace
    # Look for pattern: }[\s]*}[\s]*@media (max-width: 480px)
    pattern = r'(        @media \(max-width: 640px\) \{.*?)(        \}\s*@media \(max-width: 480px\))'
    
    def replacement(match):
        media_content = match.group(1)
        closing = match.group(2)
        
        # Check if mobile button optimizations already exist
        if '/* Mobile button optimizations */' in media_content:
            return match.group(0)  # Already exists, don't add
        
        return media_content + '\n' + mobile_css + '\n\n' + closing
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    return content

def main():
    for file_path in files_to_update:
        try:
            print(f"Processing: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply mobile CSS
            updated_content = add_mobile_css(content)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Updated: {file_path}")
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
    
    print("\n✅ All files processed!")

if __name__ == '__main__':
    main()
