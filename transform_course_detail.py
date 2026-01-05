#!/usr/bin/env python3
"""
Restructure course detail pages to match course-learning.html layout
Adds sidebar, breadcrumb, filter tabs (including Sertifikat), and module cards
"""
import re

# Sidebar HTML (from course-learning.html lines 117-223)
SIDEBAR_HTML = '''    <!-- Sidebar -->
    <aside id="top-bar-sidebar"
        class="fixed top-0 left-0 z-40 w-64 h-full transition-transform -translate-x-full sm:translate-x-0"
        aria-label="Sidebar">
        <div class="h-full px-3 py-4 overflow-y-auto bg-white border-e border-gray-200">
            <a href="../../index.html" class="flex items-center ps-2.5 mb-5">
                <img src="../../../assets/logo.png" alt="SIRENATA Logo" class="h-8 w-auto">
                <span class="self-center text-lg font-semibold whitespace-nowrap ms-2"
                    style="color: #13416B;">SIRENATA</span>
            </a>
            <ul class="space-y-2 font-medium">
                <li>
                    <a href="../../index.html"
                        class="flex items-center px-2 py-1.5 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors group">
                        <svg class="shrink-0 w-5 h-5 transition duration-75 group-hover:text-indigo-600"
                            aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M10 6.025A7.5 7.5 0 1 0 17.975 14H10V6.025Z" />
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M13.5 3c-.169 0-.334.014-.5.025V11h7.975c.011-.166.025-.331.025-.5A7.5 7.5 0 0 0 13.5 3Z" />
                        </svg>
                        <span class="ms-3">Dashboard</span>
                    </a>
                </li>
                <li>
                    <a href="my-courses.html"
                        class="flex items-center px-2 py-1.5 text-indigo-600 bg-purple-100 rounded-lg transition-colors group">
                        <svg class="shrink-0 w-5 h-5 text-indigo-600" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 4h12M6 4v16M6 20h12M6 20H5m13 0h1m-1 0V4m0 0h1M6 4H5M9 8h1v1H9V8Zm5 0h1v1h-1V8Zm-5 4h1v1H9v-1Zm5 0h1v1h-1v-1Zm-3 4h2a1 1 0 0 1 1 1v4h-4v-4a1 1 0 0 1 1-1Z" />
                        </svg>
                        <span class="flex-1 ms-3 whitespace-nowrap">Kursus Saya</span>
                    </a>
                </li>
                <li>
                    <a href="#"
                        class="flex items-center px-2 py-1.5 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors group">
                        <svg class="shrink-0 w-5 h-5 transition duration-75 group-hover:text-indigo-600"
                            aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M9.143 4H4.857A.857.857 0 0 0 4 4.857v4.286c0 .473.384.857.857.857h4.286A.857.857 0 0 0 10 9.143V4.857A.857.857 0 0 0 9.143 4Zm10 0h-4.286a.857.857 0 0 0-.857.857v4.286c0 .473.384.857.857.857h4.286A.857.857 0 0 0 20 9.143V4.857A.857.857 0 0 0 19.143 4Zm-10 10H4.857a.857.857 0 0 0-.857.857v4.286c0 .473.384.857.857.857h4.286a.857.857 0 0 0 .857-.857v-4.286A.857.857 0 0 0 9.143 14Zm10 0h-4.286a.857.857 0 0 0-.857.857v4.286c0 .473.384.857.857.857h4.286a.857.857 0 0 0 .857-.857v-4.286a.857.857 0 0 0-.857-.857Z" />
                        </svg>
                        <span class="flex-1 ms-3 whitespace-nowrap">Katalog</span>
                    </a>
                </li>
                <li>
                    <a href="../library/index.html"
                        class="flex items-center px-2 py-1.5 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors group">
                        <svg class="shrink-0 w-5 h-5 transition duration-75 group-hover:text-indigo-600"
                            aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 6.03v13m0-13c-2.819-.831-4.715-1.076-8.029-1.023A.99.99 0 0 0 3 6v11c0 .563.466 1.014 1.03 1.007 3.122-.043 5.018.212 7.97 1.023m0-13c2.819-.831 4.715-1.076 8.029-1.023A.99.99 0 0 1 21 6v11c0 .563-.466 1.014-1.03 1.007-3.122-.043-5.018.212-7.97 1.023" />
                        </svg>
                        <span class="flex-1 ms-3 whitespace-nowrap">Perpustakaan</span>
                    </a>
                </li>
                <li>
                    <button data-dropdown-toggle="dropdown-perhitungan"
                        class="flex items-center justify-between w-full px-2 py-1.5 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors group">
                        <div class="flex items-center">
                            <svg class="shrink-0 w-5 h-5 transition duration-75 group-hover:text-indigo-600"
                                aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                                viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2" d="M12 4v16m8-8H4m8-4h.01M12 16h.01M16 12h.01M8 12h.01" />
                            </svg>
                            <span class="flex-1 ms-3 whitespace-nowrap">Perhitungan</span>
                        </div>
                        <svg class="w-3 h-3 transition-transform dropdown-arrow" fill="none" stroke="currentColor"
                            viewBox="0 0 10 6">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4" />
                        </svg>
                    </button>
                    <ul id="dropdown-perhitungan" class="hidden py-2 space-y-2">
                        <li>
                            <a href="../../tim/perhitungan.html"
                                class="flex items-center w-full px-2 py-1.5 ps-10 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors">
                                Kalkulator RTK
                            </a>
                        </li>
                        <li>
                            <a href="../../tim/draft.html"
                                class="flex items-center w-full px-2 py-1.5 ps-10 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors">
                                Draft RTK
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="../support/help.html"
                        class="flex items-center px-2 py-1.5 text-gray-500 rounded-lg hover:bg-purple-100 hover:text-indigo-600 transition-colors group">
                        <svg class="shrink-0 w-5 h-5 transition duration-75 group-hover:text-indigo-600"
                            aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 13V8m0 8h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                        <span class="flex-1 ms-3 whitespace-nowrap">Bantuan</span>
                    </a>
                </li>
            </ul>
        </div>
    </aside>

'''

def transform_makro_file():
    """Transform course-detail-ptk-makro.html"""
    file_path = '/home/fritz/Fritz Kevin Manurung/Work/Magang/kemnaker/user/biasa/courses/course-detail-ptk-makro.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Insert sidebar after </nav>
    content = re.sub(
        r'(</nav>)',
        r'\1\n' + SIDEBAR_HTML,
        content,
        count=1
    )
    
    # 2. Change main container from "pt-16 sm:pt-20 px-2" to sidebar layout
    content = re.sub(
        r'<div class="pt-16 sm:pt-20 px-2 sm:px-4 lg:px-8 pb-6 sm:pb-8">',
        '<div class="p-2 sm:p-4 sm:ml-64 mt-14">',
        content
    )
    
    # 3. Replace "max-w-6xl mx-auto" div with breadcrumb + new structure
    # Find the start of content after main container
    breadcrumb_and_header = '''        <div class="p-2 sm:p-6">
            <!-- Breadcrumb -->
            <nav class="flex mb-4 sm:mb-6" aria-label="Breadcrumb">
                <ol class="inline-flex items-center space-x-1">
                    <li class="inline-flex items-center">
                        <a href="../../index.html"
                            class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-indigo-600">
                            <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z">
                                </path>
                            </svg>
                        </a>
                    </li>
                    <li>
                        <div class="flex items-center">
                            <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd"
                                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                    clip-rule="evenodd"></path>
                            </svg>
                            <a href="my-courses.html" class="ml-1 text-sm font-medium text-gray-700 hover:text-indigo-600 md:ml-2">Kursus Saya</a>
                        </div>
                    </li>
                    <li>
                        <div class="flex items-center">
                            <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd"
                                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                    clip-rule="evenodd"></path>
                            </svg>
                            <span class="ml-1 text-sm font-medium text-gray-500 md:ml-2">PTK Makro</span>
                        </div>
                    </li>
                </ol>
            </nav>

            <!-- Course Header -->
            <div class="bg-gradient-to-r from-emerald-600 to-teal-600 rounded-lg p-4 sm:p-6 text-white mb-4 sm:mb-6">
                <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3 sm:gap-0">
                    <div class="flex-1">
                        <span class="inline-flex items-center px-2 sm:px-3 py-1 rounded-full text-xs sm:text-sm font-semibold bg-white/20 mb-2 sm:mb-3">
                            ✅ Selesai
                        </span>
                        <h1 class="text-lg sm:text-2xl font-bold mb-1 sm:mb-2">Perencanaan Tenaga Kerja Makro</h1>
                        <div class="flex items-center gap-4 sm:gap-6 text-xs sm:text-sm">
                            <span>📚 8 Modul</span>
                            <span>🎓 Sertifikat Tersedia</span>
                        </div>
                    </div>
                    <div class="self-end sm:self-auto sm:ml-4">
                        <div class="bg-white/20 backdrop-blur-sm rounded-lg p-3 sm:p-4 text-center min-w-[80px] sm:min-w-[100px]">
                            <div class="text-xl sm:text-3xl font-bold">100%</div>
                            <div class="text-xs sm:text-sm">Selesai</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Filter Tabs -->
            <div class="mb-4 sm:mb-6">
                <div class="border-b border-gray-200">
                    <nav class="flex space-x-2 sm:space-x-4 overflow-x-auto pb-2 scrollbar-hide -mx-2 px-2">
                        <button onclick="filterModules('all')" id="filter-all"
                            class="filter-tab border-b-2 border-indigo-600 text-indigo-600 py-2 sm:py-3 px-1 text-xs sm:text-sm font-semibold whitespace-nowrap">
                            Semua (8)
                        </button>
                        <button onclick="filterModules('incomplete')\" id="filter-incomplete"
                            class="filter-tab border-b-2 border-transparent text-gray-500 hover:text-gray-700 py-2 sm:py-3 px-1 text-xs sm:text-sm font-medium whitespace-nowrap">
                            Sedang Berjalan (0)
                        </button>
                        <button onclick="filterModules('completed')" id="filter-completed"
                            class="filter-tab border-b-2 border-transparent text-gray-500 hover:text-gray-700 py-2 sm:py-3 px-1 text-xs sm:text-sm font-medium whitespace-nowrap">
                            Selesai (8)
                        </button>
                        <button onclick="filterModules('certificate')" id="filter-certificate"
                            class="filter-tab border-b-2 border-transparent text-gray-500 hover:text-gray-700 py-2 sm:py-3 px-1 text-xs sm:text-sm font-medium whitespace-nowrap">
                            Sertifikat
                        </button>
                    </nav>
                </div>
            </div>
'''

    # Remove old content and insert new
    content = re.sub(
        r'<div class="max-w-6xl mx-auto">.*?<!-- Back Button -->.*?</a>.*?<!-- Course Header -->.*?</div>.*?</div>.*?<div class="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6">',
        breadcrumb_and_header + '\n            <!-- Modules List -->\n            <div class="space-y-3 sm:space-y-4" id="modules-container">',
        content,
        flags=re.DOTALL
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Transformed course-detail-ptk-makro.html")

if __name__ == '__main__':
    transform_makro_file()
    print("\n✅ Transformation complete!")
