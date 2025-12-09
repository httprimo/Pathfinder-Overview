<template>
    <MainLayout>
        <!-- Hero Section -->
        <section id="home" class="relative overflow-hidden animated-gradient text-white py-24 md:py-32 lg:py-40">
            <!-- Animated Background Elements -->
            <div class="absolute inset-0 overflow-hidden">
                <div class="absolute -top-40 -right-40 w-80 h-80 bg-white opacity-10 rounded-full blur-3xl animate-pulse"></div>
                <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-white opacity-10 rounded-full blur-3xl animate-pulse" style="animation-delay: 1s;"></div>
                <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-white opacity-5 rounded-full blur-3xl"></div>
            </div>
            
            <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center animate-fade-in-up">
                    <div class="inline-block mb-6">
                        <span class="glass px-4 py-2 rounded-full text-sm font-medium backdrop-blur-md flex items-center gap-2">
                            <Icon name="rocket" :size="16" class="text-white" />
                            Research Platform
                        </span>
                    </div>
                    <h1 class="text-6xl md:text-8xl lg:text-9xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-white via-blue-100 to-white">
                        <span>{{ displayedText }}</span><span class="typing-cursor">|</span>
                    </h1>
                    <p class="text-xl md:text-2xl lg:text-3xl mb-10 text-white/90 max-w-3xl mx-auto font-light leading-relaxed">
                        A Tag-Based Career and Training Matching Platform
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                        <a 
                            href="https://development-pathfinder.onrender.com/auth/login"
                            target="_blank"
                            rel="noopener noreferrer"
                            class="group relative px-8 py-4 bg-white text-customButton rounded-xl font-semibold overflow-hidden transition-all duration-300 transform hover:scale-105 shadow-2xl hover:shadow-white/20"
                        >
                            <span class="relative z-10">Visit Main System</span>
                            <div class="absolute inset-0 bg-gradient-to-r from-blue-gray to-white opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        </a>
                        <a 
                            href="#features"
                            class="group px-8 py-4 glass border-2 border-white/30 text-white rounded-xl font-semibold backdrop-blur-md hover:bg-white/20 transition-all duration-300 transform hover:scale-105 shadow-xl"
                        >
                            Explore Features
                            <span class="inline-block ml-2 transform group-hover:translate-x-1 transition-transform">→</span>
                        </a>
                    </div>
                </div>
            </div>
            
            <!-- Scroll Indicator -->
            <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
                <svg class="w-6 h-6 text-white/70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                </svg>
            </div>
        </section>

        <!-- Quick Overview Section -->
        <section id="overview" class="relative py-20 md:py-28 bg-gradient-to-b from-white via-gray-50 to-white scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Overview"
                    subtitle="A brief introduction to our research project and its significance"
                />
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto mb-12">
                    <div class="group relative p-8 rounded-2xl bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 card-hover border border-blue-100/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-blue-200/20 rounded-full blur-2xl -mr-16 -mt-16"></div>
                        <div class="relative z-10">
                            <div class="mb-6 transform group-hover:scale-110 transition-transform duration-300">
                                <Icon name="chart" :size="64" class="text-blue-600" />
                            </div>
                            <h3 class="text-2xl font-bold mb-4 text-gray-900">ISO/IEC 25010 Evaluation</h3>
                            <p class="text-gray-700 mb-6 leading-relaxed">
                            Evaluate the developed system based on selected ISO/IEC 25010 software quality characteristics:
                        </p>
                            <ul class="text-left text-gray-600 space-y-3">
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-blue-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Functional Suitability:</strong> System accuracy and completeness</span>
                            </li>
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-blue-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Compatibility:</strong> Interoperability and co-existence</span>
                            </li>
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-blue-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Usability:</strong> User experience and learnability</span>
                            </li>
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-blue-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Security:</strong> Confidentiality and integrity</span>
                            </li>
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-blue-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Portability:</strong> Adaptability and installability</span>
                            </li>
                        </ul>
                        </div>
                    </div>
                    
                    <div class="group relative p-8 rounded-2xl bg-gradient-to-br from-emerald-50 via-green-50 to-teal-50 card-hover border border-green-100/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-green-200/20 rounded-full blur-2xl -mr-16 -mt-16"></div>
                        <div class="relative z-10">
                            <div class="mb-6 transform group-hover:scale-110 transition-transform duration-300">
                                <Icon name="users" :size="64" class="text-green-600" />
                            </div>
                            <h3 class="text-2xl font-bold mb-4 text-gray-900">USE Questionnaire Assessment</h3>
                            <p class="text-gray-700 mb-6 leading-relaxed">
                            Assess the users' perception of the system's effectiveness using the USE (Usefulness, Satisfaction, and Ease of Use) Questionnaire.
                        </p>
                            <ul class="text-left text-gray-600 space-y-3">
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-green-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Usefulness:</strong> Perceived value and capability</span>
                            </li>
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-green-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Satisfaction:</strong> User contentment and preference</span>
                            </li>
                            <li class="flex items-start">
                                    <svg class="w-5 h-5 text-green-600 mr-3 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                    </svg>
                                <span><strong>Ease of Use:</strong> Simplicity and learnability</span>
                            </li>
                        </ul>
                        </div>
                    </div>
                </div>
                
                <div class="relative p-8 md:p-12 rounded-3xl bg-gradient-to-br from-purple-50 via-pink-50 to-indigo-50 border border-purple-200/50 shadow-xl max-w-4xl mx-auto overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-purple-200/30 rounded-full blur-3xl -mr-32 -mt-32"></div>
                    <div class="relative z-10 text-center">
                        <div class="inline-block mb-6 transform hover:scale-110 transition-transform duration-300">
                            <Icon name="target" :size="80" class="text-purple-600" />
                        </div>
                        <h3 class="text-3xl font-bold mb-6 text-gray-900">Research Focus</h3>
                        <p class="text-gray-700 leading-relaxed mb-6 text-lg">
                            This study aims to develop a career and training-matching web application that automatically matches the target career selected by the applicant with training posts that have similar tags. The system will be created using the <strong class="text-purple-700">RAD (Rapid Application Development)</strong> model.
                        </p>
                        <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-white/50">
                            <p class="text-gray-700 leading-relaxed">
                                <strong class="text-purple-700">Abstract:</strong> Pathfinder addresses the prevailing issue of skills mismatch in the labor market by providing a web-based career and training-matching application. The system features a unique Career-Training Matching Engine that links applicant career goals with specific training tags. Evaluated by 34 end-users and 13 IT experts, Pathfinder achieved an overall rating of "Strongly Agree" (4.55) from end-users and "Agree" (4.07) from experts, confirming it successfully provides a centralized, zero-cost platform that empowers the workforce and bridges the gap between education and employment.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="About the Research"
                    subtitle="Understanding the background and significance of our project"
                />

                <!-- Research Background -->
                <div class="mb-16">
                    <div class="bg-gradient-to-r from-blue-gray to-blue-gray rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Research Background</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            The global landscape of hiring is undergoing a transformation, shifting away from a system that prioritizes educational credentials toward one that values demonstrable competency. This "skills-first" paradigm prioritizes knowledge and abilities over formal degrees, designed to expand talent pools and improve how people are matched to jobs.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Despite these shifts, the hiring process is still filled with conflicts. Employers struggle to identify the right talent, often relying on ambiguous and overstuffed job postings that fail to articulate precise requirements. Qualified candidates often get discouraged and preemptively exclude themselves from the application process. This issue is particularly acute in developing economies like the Philippines, which has a documented history of labor mismatch where workers are frequently over-skilled or under-skilled, lacking the requisite competencies for their current roles.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            Statistical data confirms the severity of this structural gap. Approximately 35% of workers in OECD countries are mismatched by qualification. In the Philippines, studies regarding Technical Vocational and Livelihood (TVL) graduates in Butuan City revealed a mismatch incidence of 64%, indicating a severe failure to align educational specialization with employment outcomes. Furthermore, national data indicates that youth unemployment rates have reached 13.5%, more than double the national average.
                        </p>
                    </div>
                </div>

                <!-- Importance Section -->
                <div class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Why This Research Matters</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="border-l-4 border-customButton pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Addresses Skills Mismatch</h4>
                            <p class="text-gray-600">
                                When the workforce disconnects from market needs, vulnerable populations suffer the most, facing career trajectories defined by lower lifetime earnings and reduced job satisfaction. On a macroeconomic scale, this skills mismatch serves as a primary driver of productivity loss.
                            </p>
                        </div>
                        <div class="border-l-4 border-customblue pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Zero-Cost Access</h4>
                            <p class="text-gray-600">
                                While digital platforms function as primary intermediaries in the labor market, accessing high-quality training necessary to bridge skill gaps is often financially prohibitive. Pathfinder provides a direct economic intervention by curating zero-cost resources, thereby promoting equity.
                            </p>
                        </div>
                        <div class="border-l-4 border-customdarkblue pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Skills-Based Hiring Benefits</h4>
                            <p class="text-gray-600">
                                Research indicates that non-degreed workers hired into roles based on skills demonstrate a 10-percentage point higher retention rate and realize a 25% salary increase compared to their previous roles. Enabling a genuine skills-based hiring approach is mutually beneficial.
                            </p>
                        </div>
                        <div class="border-l-4 border-customButton pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Centralized Platform</h4>
                            <p class="text-gray-600">
                                The study addresses the need for a centralized platform to access different organizations' training programs that increase job prospects in a competitive job market. By combining various training programs and career opportunities into a user-friendly web application, Pathfinder empowers college students and job seekers.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Problem Statement -->
                <div class="bg-red-50 border-l-4 border-red-500 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Problem Statement</h3>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        Existing workforce technologies, such as machine learning-based career guidance systems, have demonstrated viability in offering tailored career suggestions. However, a critical research gap remains regarding the convergence of functional specificity and economic accessibility. Current platforms often fail to provide a standardized, automated linkage between employer skill demands and cost-free skill acquisition pathways.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        There is a distinct need for systems that enhance "skill signaling," explicitly linking required KSAs (Knowledge, Skills, and Abilities) to recognized credentials, to assist candidates in understanding which skills yield labor market value. Furthermore, many firms that claim to remove degree requirements fail to alter their actual hiring behavior, often because they lack the internal processes to validate skills without educational proxies.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed">
                        While social media platforms and job portals exist, they lack integration with training or skill development resources that are crucial for enhancing an applicant's employability. These systems provide minimal to no support to users when it comes to skill development because they focus heavily on matching applicants with employers. This highlights the need for a unified platform that not only connects users with job opportunities but also empowers them to upskill and prepare through accessible training programs.
                    </p>
                </div>
            </div>
        </section>

        <!-- Objectives Section -->
        <section id="objectives" class="py-16 bg-white scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Objectives"
                    subtitle="Clear goals and targets for our research project"
                />

                <!-- General Objectives -->
                <div class="mb-16">
                    <div class="bg-indigo-50 rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                            <Icon name="target" :size="32" class="mr-3 text-indigo-600" />
                            General Objectives
                        </h3>
                        <div class="space-y-4">
                            <div class="flex items-start">
                                <div class="flex-shrink-0 w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center font-semibold mr-4">
                                    1
                                </div>
                                <p class="text-gray-700 text-lg flex-1">
                                    Develop a career and training-matching web application that automatically matches the target career selected by the applicant with training posts that have similar tags. The system will be created using the RAD (Rapid Application Development) model.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Specific Objectives -->
                <div>
                    <h3 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                        <Icon name="list" :size="32" class="mr-3 text-indigo-600" />
                        Specific Objectives
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300">
                            <div class="flex items-center mb-4">
                                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mr-3">
                                    <span class="text-purple-600 font-bold">1</span>
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">Evaluate System Quality</h4>
                            </div>
                            <p class="text-gray-600 mb-3">
                                Evaluate the developed system based on selected ISO/IEC 25010 software quality characteristics:
                            </p>
                            <ul class="text-gray-600 space-y-1 text-sm ml-4">
                                <li>• <strong>Functional Suitability:</strong> System accuracy and completeness</li>
                                <li>• <strong>Compatibility:</strong> Interoperability and co-existence</li>
                                <li>• <strong>Usability:</strong> User experience and learnability</li>
                                <li>• <strong>Security:</strong> Confidentiality and integrity</li>
                                <li>• <strong>Portability:</strong> Adaptability and installability</li>
                            </ul>
                        </div>

                        <div class="bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300">
                            <div class="flex items-center mb-4">
                                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mr-3">
                                    <span class="text-purple-600 font-bold">2</span>
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">Assess User Perception</h4>
                            </div>
                            <p class="text-gray-600 mb-3">
                                Assess the users' perception of the system's effectiveness using the USE (Usefulness, Satisfaction, and Ease of Use) Questionnaire.
                            </p>
                            <ul class="text-gray-600 space-y-1 text-sm ml-4">
                                <li>• <strong>Usefulness:</strong> Perceived value and capability</li>
                                <li>• <strong>Satisfaction:</strong> User contentment and preference</li>
                                <li>• <strong>Ease of Use:</strong> Simplicity and learnability</li>
                                <li>• <strong>Ease of Learning:</strong> Quick mastery of features</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section id="features" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="System Features"
                    subtitle="Key features and capabilities of our research system"
                />

                <!-- Features Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
                    <div 
                        v-for="(feature, index) in features" 
                        :key="index"
                        class="group relative bg-white rounded-2xl p-8 card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden"
                        :style="{ animationDelay: `${index * 0.1}s` }"
                    >
                        <div class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500"></div>
                        <div class="relative z-10">
                            <div class="mb-6 transform group-hover:scale-110 group-hover:rotate-6 transition-all duration-300">
                                <div class="inline-block p-4 rounded-2xl bg-gradient-to-br from-indigo-100 to-purple-100 group-hover:from-indigo-200 group-hover:to-purple-200 transition-all duration-300">
                                    <Icon :name="feature.icon" :size="48" class="text-indigo-600" />
                                </div>
                            </div>
                            <h3 class="text-xl font-bold text-gray-900 mb-4 group-hover:text-indigo-600 transition-colors">{{ feature.title }}</h3>
                            <p class="text-gray-600 leading-relaxed">{{ feature.description }}</p>
                        </div>
                        <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></div>
                    </div>
                </div>

                <!-- System Screenshots Carousel -->
                <div class="mb-16 -mx-4 sm:-mx-6 lg:-mx-8">
                    <div class="w-full bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-50 py-8">
                        <!-- Header with Page Indicator and Navigation -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-4">
                                    <div class="bg-customButton text-white px-4 py-2 rounded-full font-semibold text-sm">
                                        Page {{ currentScreenshotStep + 1 }} of {{ screenshotSteps.length }}
                                    </div>
                                </div>
                                <div class="flex items-center gap-2">
                                    <button
                                        @click="previousScreenshotStep"
                                        :disabled="currentScreenshotStep === 0"
                                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                    >
                                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                                        </svg>
                                    </button>
                                    <button
                                        @click="nextScreenshotStep"
                                        :disabled="currentScreenshotStep === screenshotSteps.length - 1"
                                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                    >
                                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Main Content Area -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
                                <!-- Left Panel - Screenshot Display -->
                                <div class="bg-gradient-to-br from-purple-100 to-indigo-100 rounded-2xl p-8 shadow-xl">
                                    <div class="bg-white rounded-lg overflow-hidden shadow-lg group">
                                        <img
                                            :src="currentStepData?.image"
                                            :alt="currentStepData?.title || `Step ${currentScreenshotStep + 1}`"
                                            class="w-full h-auto transition-transform duration-300 ease-in-out group-hover:scale-105"
                                            @error="handleScreenshotError"
                                        />
                                    </div>
                                </div>

                                <!-- Right Panel - Description -->
                                <div class="space-y-4">
                                    <p class="text-4xl font-bold text-customButton mb-4">
                                        {{ currentStepData?.description || 'System screenshot showing key functionality.' }}
                                    </p>
                                    <div v-if="currentStepData?.details && currentStepData.details.length > 0" class="mt-6 space-y-2">
                                        <h3 class="text-xl font-semibold text-gray-800">Key Features:</h3>
                                        <ul class="list-disc list-inside space-y-1 text-gray-600">
                                            <li v-for="(detail, index) in currentStepData.details" :key="index">{{ detail }}</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pagination Dots and Progress Bar -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
                            <!-- Pagination Dots -->
                            <div class="flex justify-center items-center gap-3 mb-4 flex-wrap">
                                <button
                                    v-for="(step, index) in screenshotSteps"
                                    :key="index"
                                    @click="goToScreenshotStep(index)"
                                    class="w-10 h-10 rounded-full border-2 flex items-center justify-center font-semibold text-sm transition-all"
                                    :class="index === currentScreenshotStep 
                                        ? 'bg-customButton text-white border-customButton' 
                                        : 'bg-white text-gray-700 border-gray-300 hover:border-customButton hover:bg-purple-50'"
                                >
                                    {{ index + 1 }}
                                </button>
                            </div>

                            <!-- Progress Bar -->
                            <div class="w-full max-w-4xl mx-auto">
                                <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                                    <div
                                        class="h-full bg-customButton transition-all duration-300 ease-out"
                                        :style="{ width: `${((currentScreenshotStep + 1) / screenshotSteps.length) * 100}%` }"
                                    ></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <!-- Additional Features List -->
                <div class="bg-indigo-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Additional Features</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div 
                            v-for="(item, index) in additionalFeatures" 
                            :key="index"
                            class="flex items-center"
                        >
                            <svg class="w-6 h-6 text-indigo-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                            </svg>
                            <span class="text-gray-700">{{ item }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Methodology Section -->
        <section id="methodology" class="py-16 bg-white scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Methodology"
                    subtitle="The approach and methods used in our research"
                />

                <!-- Methodology Overview -->
                <div class="mb-16">
                    <div class="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Methodology Overview</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Pathfinder was developed using the Rapid Application Development (RAD) model, which emphasizes rapid prototyping, continuous user involvement, and iterative refinement. RAD was selected due to the project's need for consistent validation from stakeholders such as applicants and organizations.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            This model allowed the developers to transform user requirements into working prototypes, gather real-time feedback, and revise system features dynamically. RAD is particularly effective for projects where technical and business requirements must be aligned through constant feedback, as it allows the project owner to review progress after each phase.
                        </p>
                    </div>
                </div>

                <!-- Research Phases -->
                <div class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-12 text-center">Research Phases</h3>
                    <div class="space-y-6">
                        <div 
                            v-for="(phase, index) in phases" 
                            :key="index"
                            class="group relative flex flex-col md:flex-row items-start bg-white rounded-2xl p-8 card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden"
                        >
                            <div class="absolute inset-0 bg-gradient-to-r from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/30 group-hover:to-purple-50/30 transition-all duration-500"></div>
                            <div class="flex-shrink-0 w-20 h-20 bg-gradient-to-br from-indigo-600 to-purple-600 text-white rounded-2xl flex items-center justify-center font-bold text-2xl mr-6 mb-4 md:mb-0 shadow-lg transform group-hover:scale-110 group-hover:rotate-6 transition-all duration-300">
                                {{ index + 1 }}
                            </div>
                            <div class="flex-1 relative z-10">
                                <h4 class="text-2xl font-bold text-gray-900 mb-4 group-hover:text-indigo-600 transition-colors">{{ phase.title }}</h4>
                                <p class="text-gray-600 leading-relaxed">{{ phase.description }}</p>
                            </div>
                            <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></div>
                        </div>
                    </div>
                </div>

                <!-- Technologies Used -->
                <div class="bg-gray-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Technologies Used</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                        <div 
                            v-for="(tech, index) in technologies" 
                            :key="index"
                            class="bg-white rounded-lg p-6 text-center border-2 border-gray-200 hover:border-indigo-500 hover:shadow-lg transition-all duration-300"
                        >
                            <div class="mb-3 flex justify-center">
                                <div class="inline-block p-3 rounded-xl bg-gradient-to-br from-indigo-50 to-purple-50">
                                    <Icon :name="tech.icon" :size="40" class="text-indigo-600" />
                                </div>
                            </div>
                            <h4 class="font-semibold text-gray-900 mb-2">{{ tech.name }}</h4>
                            <p class="text-sm text-gray-600">{{ tech.description }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Architecture Section -->
        <section id="architecture" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="System Architecture"
                    subtitle="Diagrams and architecture overview of the system"
                />

                <!-- ERD Diagram -->
                <div class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Entity Relationship Diagram (ERD)</h3>
                    <div class="bg-gray-100 rounded-lg p-8 border-2 border-gray-300">
                        <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                            <img 
                                src="/images/architecture/erd-diagram.png" 
                                alt="Entity Relationship Diagram"
                                class="w-full h-auto"
                                @error="$event.target.style.display='none'; $event.target.nextElementSibling.style.display='flex';"
                            />
                            <!-- Fallback placeholder if image not found -->
                            <div class="aspect-video flex items-center justify-center shadow-inner" style="display: none;">
                                <div class="text-center">
                                    <svg class="w-20 h-20 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                    </svg>
                                    <p class="text-gray-500 font-medium text-lg">ERD Placeholder</p>
                                    <p class="text-gray-400 text-sm mt-2">Image not found at: <code class="text-xs bg-gray-100 px-2 py-1 rounded">public/images/architecture/erd-diagram.png</code></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- System Architecture Diagram -->
                <div class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">System Architecture Diagram</h3>
                    <div class="bg-gray-100 rounded-lg p-8 border-2 border-gray-300">
                        <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                            <img 
                                src="/images/architecture/system-architecture-diagram.png" 
                                alt="System Architecture Diagram"
                                class="w-full h-auto"
                                @error="$event.target.style.display='none'; $event.target.nextElementSibling.style.display='flex';"
                            />
                            <!-- Fallback placeholder if image not found -->
                            <div class="aspect-video flex items-center justify-center shadow-inner" style="display: none;">
                                <div class="text-center">
                                    <svg class="w-20 h-20 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                                    </svg>
                                    <p class="text-gray-500 font-medium text-lg">System Architecture Placeholder</p>
                                    <p class="text-gray-400 text-sm mt-2">Place your diagram at: <code class="text-xs bg-gray-100 px-2 py-1 rounded">public/images/architecture/system-architecture-diagram.png</code></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Architecture Description -->
                <div class="bg-indigo-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Architecture Overview</h3>
                    <div class="space-y-6">
                        <div>
                            <h4 class="text-xl font-semibold text-gray-900 mb-3">Frontend Architecture</h4>
                            <p class="text-gray-700 leading-relaxed mb-4">
                                The Pathfinder frontend is built using <strong>Vue.js</strong> as the primary JavaScript framework, providing a reactive, 
                                component-based architecture that enables dynamic user interfaces. The application leverages <strong>Tailwind CSS</strong> 
                                as a utility-first CSS framework, allowing for rapid UI development with consistent design patterns and responsive layouts 
                                that work seamlessly across desktop, tablet, and mobile devices.
                            </p>
                            <p class="text-gray-700 leading-relaxed mb-4">
                                The frontend architecture supports multiple user roles (Applicants, Organizations, and Administrators), each with 
                                distinct interfaces and functionalities. Key frontend modules include the <strong>Career-Training Matching Engine</strong> 
                                interface, which displays tag-based matches in real-time; the <strong>Resume Editor</strong> component for document 
                                creation and management; <strong>Calendar & Event Management</strong> views for scheduling training sessions and 
                                interviews; and <strong>Dashboard Analytics</strong> components that visualize engagement metrics and statistics.
                            </p>
                            <p class="text-gray-700 leading-relaxed">
                                The user interface was prototyped using <strong>Figma</strong> during the User Design Phase, ensuring that all user 
                                roles and workflows were visually validated before implementation. The frontend communicates with the backend through 
                                RESTful API endpoints, handling authentication, data fetching, file uploads, and real-time status updates. The responsive 
                                design ensures optimal user experience across all device types, with mobile-first considerations for accessibility.
                            </p>
                        </div>
                        <div>
                            <h4 class="text-xl font-semibold text-gray-900 mb-3">Backend Architecture</h4>
                            <p class="text-gray-700 leading-relaxed mb-4">
                                The backend is powered by <strong>Laravel</strong>, a robust PHP framework that provides comprehensive server-side 
                                functionality including authentication, authorization, routing, and database management. The application follows Laravel's 
                                MVC (Model-View-Controller) architectural pattern, ensuring separation of concerns and maintainable code structure.
                            </p>
                            <p class="text-gray-700 leading-relaxed mb-4">
                                The backend implements several critical systems: <strong>User Authentication & Authorization</strong> with role-based access 
                                control (RBAC) for Applicants, Organizations, and Administrators; <strong>Tag-Based Matching Algorithm</strong> that 
                                processes career goals and training tags to generate relevant matches; <strong>QR Code Generation System</strong> for 
                                attendance tracking and certificate issuance; <strong>Document Management API</strong> for handling resume uploads, 
                                certificate storage, and organization verification documents; and <strong>Email Notification System</strong> for 
                                verification, status updates, and event reminders.
                            </p>
                            <p class="text-gray-700 leading-relaxed">
                                The application is deployed on <strong>Render</strong>, a cloud platform that provides scalable hosting, automatic SSL 
                                certificates, and seamless deployment pipelines. The backend integrates with <strong>Supabase</strong> for additional 
                                backend-as-a-service capabilities, including real-time database subscriptions and file storage. The middleware stack 
                                handles CSRF protection, request validation, rate limiting, and session management to ensure security and performance.
                            </p>
                        </div>
                        <div>
                            <h4 class="text-xl font-semibold text-gray-900 mb-3">Database Design</h4>
                            <p class="text-gray-700 leading-relaxed mb-4">
                                The database architecture is built on <strong>PostgreSQL</strong>, an advanced open-source relational database management 
                                system that provides ACID compliance, robust data integrity, and support for complex queries. The database schema was 
                                designed using <strong>Lucidchart</strong> during the User Design Phase, ensuring proper normalization and optimal 
                                relationship definitions between entities.
                            </p>
                            <p class="text-gray-700 leading-relaxed mb-4">
                                The core database structure includes tables for: <strong>Users</strong> (with role differentiation for applicants, 
                                organizations, and administrators); <strong>Careers</strong> and <strong>Training Programs</strong> with associated 
                                metadata; <strong>Tags</strong> that enable the matching algorithm to link careers with relevant training opportunities; 
                                <strong>Applications</strong> and <strong>Registrations</strong> tracking user interactions; <strong>Certificates</strong> 
                                for issued credentials; <strong>Events</strong> and <strong>Calendar Entries</strong> for scheduling; and 
                                <strong>Documents</strong> for file management including resumes and verification materials.
                            </p>
                            <p class="text-gray-700 leading-relaxed">
                                The Entity Relationship Diagram (ERD) displayed above illustrates the complete database schema, showing primary keys, 
                                foreign key relationships, and the many-to-many relationships between tags, careers, and training programs that enable 
                                the matching functionality. The database design emphasizes referential integrity, with cascading updates and deletes 
                                where appropriate, and includes indexes on frequently queried fields (such as tags and user roles) to optimize 
                                query performance for the matching algorithm.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Results Section -->
        <section id="results" class="py-16 bg-white scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Results"
                    subtitle="Findings, insights, and outcomes of our research"
                />

                <!-- Key Findings -->
                <div class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Key Findings</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div 
                            v-for="(finding, index) in findings" 
                            :key="index"
                            class="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-lg p-6 border-l-4 border-indigo-600"
                        >
                            <div class="flex items-center mb-3">
                                <div class="w-10 h-10 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold mr-3">
                                    {{ index + 1 }}
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">{{ finding.title }}</h4>
                            </div>
                            <p class="text-gray-700">{{ finding.description }}</p>
                        </div>
                    </div>
                </div>

                <!-- Results Summary -->
                <div class="mb-16">
                    <div class="bg-green-50 border-l-4 border-green-500 rounded-lg p-8 md:p-12">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Results Summary</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            The Pathfinder web application was successfully constructed using the Rapid Application Development (RAD) model, achieving stable and reliable deployment from local development to live production environment on Render. The project successfully implemented all intended software modules designed to bridge the gap between skill acquisition and employment.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Key features including the Career-Training Matching Engine, Resume Editor, and QR code-based attendance and certificate issuance system effectively digitized processes that were previously done manually. The system was validated against ISO/IEC 25010 and USE model standards, confirming that Pathfinder is a significant improvement over existing disjointed platforms.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            Ultimately, this project addresses the critical economic challenge of skills mismatch in the localized labor market of Tuguegarao City. By providing a zero-cost, centralized platform that links skills-first training opportunities directly to career paths, Pathfinder empowers vulnerable populations—specifically unemployed youth and low-income job seekers—to enhance their employability without financial barriers.
                        </p>
                    </div>
                </div>

                <!-- Insights -->
                <div class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Key Insights</h3>
                    <div class="space-y-6">
                        <div 
                            v-for="(insight, index) in insights" 
                            :key="index"
                            class="flex items-start bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300"
                        >
                            <div class="flex-shrink-0 w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mr-4">
                                <Icon name="lightbulb" :size="24" class="text-purple-600" />
                            </div>
                            <div class="flex-1">
                                <h4 class="text-lg font-semibold text-gray-900 mb-2">{{ insight.title }}</h4>
                                <p class="text-gray-600">{{ insight.description }}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Statistics or Metrics -->
                <div class="relative bg-gradient-to-br from-gray-50 via-indigo-50/30 to-purple-50/30 rounded-3xl p-8 md:p-12 border border-gray-200/50 shadow-xl overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-indigo-200/20 rounded-full blur-3xl -mr-32 -mt-32"></div>
                    <div class="relative z-10">
                        <h3 class="text-3xl font-bold text-gray-900 mb-12 text-center">Research Metrics</h3>
                        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                            <div 
                                v-for="(metric, index) in metrics" 
                                :key="index"
                                class="group relative bg-white rounded-2xl p-6 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden"
                            >
                                <div class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500"></div>
                                <div class="relative z-10">
                                    <div class="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent mb-3 transform group-hover:scale-110 transition-transform duration-300">
                                        {{ metric.value }}
                                    </div>
                                    <div class="text-gray-600 text-xs md:text-sm leading-tight">{{ metric.label }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Team Section -->
        <section id="team" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Our Team"
                    subtitle="The developers and researchers behind this project"
                />

                <!-- Team Members (Students) - 4 aligned -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
                    <div 
                        v-for="(member, index) in students" 
                        :key="index"
                        class="group relative bg-white rounded-2xl p-8 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden"
                    >
                        <div class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500"></div>
                        <div class="relative z-10">
                            <div class="w-32 h-32 mx-auto mb-6 flex items-center justify-center overflow-hidden rounded-2xl border-4 border-gray-200 group-hover:border-indigo-400 transition-all duration-300 transform group-hover:scale-110 group-hover:rotate-3 shadow-lg">
                                <img 
                                    v-if="member.image" 
                                    :src="member.image" 
                                    :alt="member.name"
                                    class="w-full h-full object-cover"
                                />
                                <div 
                                    v-else
                                    class="w-full h-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white text-4xl font-bold"
                                >
                                    {{ member.initials }}
                                </div>
                            </div>
                            <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">{{ member.name }}</h3>
                            <p class="text-indigo-600 font-semibold mb-2">{{ member.role }}</p>
                            <p class="text-gray-600 text-sm mb-2">{{ member.course }}</p>
                            <p class="text-gray-500 text-xs mb-6">{{ member.location }}</p>
                            <div class="flex justify-center">
                                <a 
                                    v-if="member.email"
                                    :href="`mailto:${member.email}`"
                                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 hover:bg-indigo-600 hover:text-white transition-all duration-300 transform hover:scale-110"
                                    :title="member.email"
                                >
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Adviser and Instructor - Side by side at the bottom -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-16 max-w-5xl mx-auto">
                    <!-- Adviser -->
                    <div class="group relative bg-white rounded-2xl p-8 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500"></div>
                        <div class="relative z-10">
                            <div class="w-36 h-36 mx-auto mb-6 flex items-center justify-center overflow-hidden rounded-2xl border-4 border-gray-200 group-hover:border-indigo-400 transition-all duration-300 transform group-hover:scale-110 group-hover:rotate-3 shadow-lg">
                                <img 
                                    v-if="adviser.image" 
                                    :src="adviser.image" 
                                    :alt="adviser.name"
                                    class="w-full h-full object-cover"
                                />
                                <div 
                                    v-else
                                    class="w-full h-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white text-5xl font-bold"
                                >
                                    {{ adviser.initials }}
                                </div>
                            </div>
                            <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">{{ adviser.name }}</h3>
                            <p class="text-indigo-600 font-semibold mb-2">{{ adviser.role }}</p>
                            <p class="text-gray-600 text-sm mb-2" v-if="adviser.course">{{ adviser.course }}</p>
                            <p class="text-gray-500 text-xs mb-6">{{ adviser.location }}</p>
                            <div class="flex justify-center">
                                <a 
                                    v-if="adviser.email"
                                    :href="`mailto:${adviser.email}`"
                                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 hover:bg-indigo-600 hover:text-white transition-all duration-300 transform hover:scale-110"
                                    :title="adviser.email"
                                >
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Instructor -->
                    <div class="group relative bg-white rounded-2xl p-8 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500"></div>
                        <div class="relative z-10">
                            <div class="w-36 h-36 mx-auto mb-6 flex items-center justify-center overflow-hidden rounded-2xl border-4 border-gray-200 group-hover:border-indigo-400 transition-all duration-300 transform group-hover:scale-110 group-hover:rotate-3 shadow-lg">
                                <img 
                                    v-if="instructor.image" 
                                    :src="instructor.image" 
                                    :alt="instructor.name"
                                    class="w-full h-full object-cover"
                                />
                                <div 
                                    v-else
                                    class="w-full h-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white text-5xl font-bold"
                                >
                                    {{ instructor.initials }}
                                </div>
                            </div>
                            <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">{{ instructor.name }}</h3>
                            <p class="text-indigo-600 font-semibold mb-2">{{ instructor.role }}</p>
                            <p class="text-gray-600 text-sm mb-2" v-if="instructor.course">{{ instructor.course }}</p>
                            <p class="text-gray-500 text-xs mb-6" v-if="instructor.location">{{ instructor.location }}</p>
                            <div class="flex justify-center">
                                <a 
                                    v-if="instructor.email"
                                    :href="`mailto:${instructor.email}`"
                                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 hover:bg-indigo-600 hover:text-white transition-all duration-300 transform hover:scale-110"
                                    :title="instructor.email"
                                >
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Team Description -->
                <div class="bg-indigo-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">About Our Team</h3>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        Our team consists of dedicated BSIT-4 students and an experienced adviser working together 
                        to develop Pathfinder, a tag-based career and training matching platform. Each team member 
                        brings unique skills and perspectives to ensure the success of this research project.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed">
                        The project is being conducted under the guidance of our adviser, Mr. Jerome S. Miguel, 
                        who provides valuable insights and mentorship throughout the development process. 
                        Our team members are distributed across different locations in Isabela and Cagayan, 
                        demonstrating effective collaboration despite geographical distances.
                    </p>
                </div>
            </div>
        </section>
    </MainLayout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';
import Icon from '@/Components/Icon.vue';

const displayedText = ref('');
const fullText = 'Pathfinder';
const typingSpeed = 150;
const erasingSpeed = 100;
const pauseAfterTyping = 2000;
const pauseAfterErasing = 500;

// Features data
const features = ref([
    {
        icon: 'target',
        title: 'Career-Training Matching Engine',
        description: 'Automatically matches the target career selected by applicants with training posts that have similar tags, helping users find relevant skill development opportunities aligned with their career goals.'
    },
    {
        icon: 'document',
        title: 'Resume Editor',
        description: 'Streamlines document preparation by allowing applicants to generate professional resumes with fields for professional summary, experience, education, and skills. Includes certificate management integration.'
    },
    {
        icon: 'calendar',
        title: 'Calendar & Event Management',
        description: 'Displays scheduled training events and interview dates. Applicants can view their registered trainings and applied careers, while organizations can manage their event schedules efficiently.'
    },
    {
        icon: 'search',
        title: 'Advanced Search & Filtering',
        description: 'Multi-filter search functionality allowing users to search for careers, trainings, and organizations. The search bar contains three filters: career, training, and organization for precise results.'
    },
    {
        icon: 'check',
        title: 'QR Code Attendance System',
        description: 'QR code-based attendance and certificate issuance system that digitizes processes previously done manually. Organizations can generate QR codes for training sessions and issue certificates to eligible participants.'
    },
    {
        icon: 'users',
        title: 'Organization Verification',
        description: 'Administrative workflow for verifying organization accounts. Organizations must submit required documents for verification before they can post trainings and career opportunities, ensuring platform credibility.'
    },
    {
        icon: 'chart',
        title: 'Dashboard Analytics',
        description: 'Organization dashboard displays statistics for career and training posts, providing insights into registrations, applications, and overall engagement metrics.'
    },
    {
        icon: 'document',
        title: 'Document Management',
        description: 'Applicants can upload and manage certificates obtained outside the system, and include them in their resume. The system also tracks certificates issued by organizations for trainings attended within the platform.'
    },
    {
        icon: 'briefcase',
        title: 'Application Tracking',
        description: 'Applicants can track the status of their career applications (submitted, for review, for interview, hired/declined) and training registrations (upcoming, ongoing, conducted).'
    }
]);

const additionalFeatures = ref([
    'User Registration & Authentication (Applicants, Organizations, Admin)',
    'Email Verification System',
    'Profile Management & Account Settings',
    'Training Post Creation & Management',
    'Career Opportunity Posting & Management',
    'Interview Scheduling System',
    'Certificate Generation & Issuance',
    'Activity Tracking & History',
    'Multi-role Access Control',
    'Responsive Web Design',
    'Real-time Status Updates',
    'Secure File Upload & Storage'
]);

// System Screenshots Steps - All 27 pages from the User Manual PDF
const screenshotSteps = ref([
    {
        title: 'Page 1',
        description: 'User Manual - Introduction and overview of the PATHFINDER system.',
        image: '/images/screenshots/page-01.png'
    },
    {
        title: 'Page 2',
        description: 'System features and key functionalities.',
        image: '/images/screenshots/page-02.png'
    },
    {
        title: 'Page 3',
        description: 'User interface and navigation guide.',
        image: '/images/screenshots/page-03.png'
    },
    {
        title: 'Page 4',
        description: 'Registration and account creation process.',
        image: '/images/screenshots/page-04.png'
    },
    {
        title: 'Page 5',
        description: 'Login and authentication procedures.',
        image: '/images/screenshots/page-05.png'
    },
    {
        title: 'Page 6',
        description: 'Dashboard overview and main features.',
        image: '/images/screenshots/page-06.png'
    },
    {
        title: 'Page 7',
        description: 'Profile management and settings.',
        image: '/images/screenshots/page-07.png'
    },
    {
        title: 'Page 8',
        description: 'Career search and browsing functionality.',
        image: '/images/screenshots/page-08.png'
    },
    {
        title: 'Page 9',
        description: 'Training search and filtering options.',
        image: '/images/screenshots/page-09.png'
    },
    {
        title: 'Page 10',
        description: 'Resume builder and editor features.',
        image: '/images/screenshots/page-10.png'
    },
    {
        title: 'Page 11',
        description: 'Application tracking and status monitoring.',
        image: '/images/screenshots/page-11.png'
    },
    {
        title: 'Page 12',
        description: 'Calendar view and event management.',
        image: '/images/screenshots/page-12.png'
    },
    {
        title: 'Page 13',
        description: 'Certificate management and upload.',
        image: '/images/screenshots/page-13.png'
    },
    {
        title: 'Page 14',
        description: 'Organization dashboard and analytics.',
        image: '/images/screenshots/page-14.png'
    },
    {
        title: 'Page 15',
        description: 'Training post creation and management.',
        image: '/images/screenshots/page-15.png'
    },
    {
        title: 'Page 16',
        description: 'Career posting and management tools.',
        image: '/images/screenshots/page-16.png'
    },
    {
        title: 'Page 17',
        description: 'QR code attendance system.',
        image: '/images/screenshots/page-17.png'
    },
    {
        title: 'Page 18',
        description: 'Certificate generation and issuance.',
        image: '/images/screenshots/page-18.png'
    },
    {
        title: 'Page 19',
        description: 'Interview scheduling and management.',
        image: '/images/screenshots/page-19.png'
    },
    {
        title: 'Page 20',
        description: 'Search and filtering functionality.',
        image: '/images/screenshots/page-20.png'
    },
    {
        title: 'Page 21',
        description: 'Tag-based matching system.',
        image: '/images/screenshots/page-21.png'
    },
    {
        title: 'Page 22',
        description: 'Organization verification process.',
        image: '/images/screenshots/page-22.png'
    },
    {
        title: 'Page 23',
        description: 'Admin panel and user management.',
        image: '/images/screenshots/page-23.png'
    },
    {
        title: 'Page 24',
        description: 'System settings and configuration.',
        image: '/images/screenshots/page-24.png'
    },
    {
        title: 'Page 25',
        description: 'Notifications and messaging system.',
        image: '/images/screenshots/page-25.png'
    },
    {
        title: 'Page 26',
        description: 'Help and support documentation.',
        image: '/images/screenshots/page-26.png'
    },
    {
        title: 'Page 27',
        description: 'Appendix and additional resources.',
        image: '/images/screenshots/page-27.png'
    }
]);

// Carousel state
const currentScreenshotStep = ref(0);

// Computed property for current step data
const currentStepData = computed(() => {
    return screenshotSteps.value[currentScreenshotStep.value] || null;
});

// Navigation functions
const nextScreenshotStep = () => {
    if (currentScreenshotStep.value < screenshotSteps.value.length - 1) {
        currentScreenshotStep.value++;
    }
};

const previousScreenshotStep = () => {
    if (currentScreenshotStep.value > 0) {
        currentScreenshotStep.value--;
    }
};

const goToScreenshotStep = (index) => {
    if (index >= 0 && index < screenshotSteps.value.length) {
        currentScreenshotStep.value = index;
    }
};

const handleScreenshotError = (event) => {
    event.target.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="800" height="600"%3E%3Crect fill="%23f3f4f6" width="800" height="600"/%3E%3Ctext x="50%25" y="50%25" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="24" fill="%239ca3af"%3EScreenshot not found%3C/text%3E%3C/svg%3E';
};

// Keyboard navigation
let keyboardHandler = null;

onMounted(() => {
    keyboardHandler = (e) => {
        if (e.key === 'ArrowLeft') {
            previousScreenshotStep();
        } else if (e.key === 'ArrowRight') {
            nextScreenshotStep();
        }
    };
    window.addEventListener('keydown', keyboardHandler);
});

onUnmounted(() => {
    if (keyboardHandler) {
        window.removeEventListener('keydown', keyboardHandler);
    }
});


// Methodology data
const phases = ref([
    {
        title: 'Requirements Planning Phase',
        description: 'The project proposal and initial concepts were presented to target administrators. Requirements were gathered through interviews with representatives from the Department of Information and Communications Technology (DICT) Region II. Administrators described their existing workflows, enabling developers to validate requirements and align system functionalities with national standards and organizational processes.'
    },
    {
        title: 'User Design Phase',
        description: 'Developers translated validated requirements into logical and visual designs. Two primary tools were utilized: Figma for creating detailed UI/UX prototypes illustrating how distinct user roles (applicants, organizations, administrators) would navigate the web application, and Lucidchart for designing the database schema to visualize entity relationships and ensure the data structure could support complex queries.'
    },
    {
        title: 'Construction Phase',
        description: 'Development transitioned to implementation using a modern web development stack: Frontend (Vue.js and Tailwind CSS), Backend (Laravel), and Database & Storage (PostgreSQL and Supabase). The development followed an iterative cycle, where modules were built, tested, and revised based on continuous feedback to ensure seamless integration of stack components.'
    },
    {
        title: 'Cutover Phase',
        description: 'The web application underwent rigorous testing and validation. The system was presented to a panel of distinct organizations (DICT Region II, Center for Digital Transformation - USLT, and TESDA Region II) to assess alignment with operational needs. All inputs and recommendations were synthesized and implemented. Following refinements, the web application was deployed online using Render to ensure live accessibility in a production environment.'
    }
]);

const technologies = ref([
    { icon: 'vue', name: 'Vue.js', description: 'Frontend framework for building user interfaces' },
    { icon: 'palette', name: 'Tailwind CSS', description: 'Utility-first CSS framework for styling' },
    { icon: 'tools', name: 'Laravel', description: 'PHP backend framework for web applications' },
    { icon: 'database', name: 'PostgreSQL', description: 'Advanced open-source relational database' },
    { icon: 'cloud', name: 'Supabase', description: 'Backend-as-a-Service for database and storage' },
    { icon: 'rocket', name: 'Render', description: 'Cloud platform for deployment and hosting' },
    { icon: 'design', name: 'Figma', description: 'Design tool for UI/UX prototyping' },
    { icon: 'chart', name: 'Lucidchart', description: 'Database schema design and visualization' }
]);

// Results data
const findings = ref([
    {
        title: 'High End-User Satisfaction',
        description: 'The web application achieved an overall mean rating of 4.55 (Strongly Agree) from 34 end-users, with "Ease of Use" receiving the highest individual score of 4.64. This indicates that the interface design was highly intuitive for college students and job seekers.'
    },
    {
        title: 'Strong Technical Quality',
        description: 'Evaluation by 13 IT experts yielded an overall mean of 4.07 (Agree) based on ISO/IEC 25010 standards, with "Portability" scoring highest at 4.15, confirming the system\'s adaptability across different operational environments.'
    },
    {
        title: 'Excellent Usability Metrics',
        description: 'All USE Questionnaire criteria received "Strongly Agree" ratings: Usefulness (4.63), Ease of Use (4.64), Ease of Learning (4.51), and Satisfaction (4.43). Users could quickly master the web application functionalities without extensive instruction.'
    },
    {
        title: 'Comprehensive Quality Standards',
        description: 'All ISO/IEC 25010 characteristics received "Agree" ratings: Functional Suitability (4.03), Compatibility (4.08), Usability (4.08), Security (4.00), and Portability (4.15), confirming the system successfully met its objectives.'
    }
]);

const insights = ref([
    {
        title: 'User-Centric Design Success',
        description: 'The high "Ease of Use" rating (4.64) demonstrates that the interface design, specifically the navigation flows for searching careers and trainings, was intuitive for the target audience. This validates the effectiveness of the RAD methodology\'s emphasis on continuous user involvement and iterative refinement.'
    },
    {
        title: 'Centralized Platform Value',
        description: 'The "Usefulness" rating of 4.63 confirms that respondents found the web application\'s core purpose of centralizing training and career opportunities highly relevant to their needs. This addresses the critical gap in existing platforms that require users to navigate multiple websites.'
    },
    {
        title: 'Technical Adaptability',
        description: 'The highest-rated ISO 25010 characteristic was "Portability" (4.15), indicating that experts found the web application adaptable across different environments and devices. This confirms the system\'s readiness for broader deployment beyond Tuguegarao City.'
    },
    {
        title: 'Skills-Based Approach Validation',
        description: 'The positive evaluation results validate Pathfinder\'s approach to skills-based hiring. The system successfully provides a centralized, secure, and compatible platform that effectively replaces the need to navigate multiple websites for training and job applications, addressing the skills mismatch challenge.'
    }
]);

const metrics = ref([
    { value: '4.55', label: 'Overall End-User Rating (Strongly Agree)' },
    { value: '4.64', label: 'Ease of Use Score (Highest)' },
    { value: '34', label: 'End-User Evaluators' },
    { value: '13', label: 'IT Expert Evaluators' },
    { value: '4.07', label: 'Overall Expert Rating (Agree)' },
    { value: '4.15', label: 'Portability Score (Highest)' }
]);

// Team data
const students = ref([
    {
        name: 'JERALD BON HARRIS V. AGUSTIN',
        initials: 'JA',
        role: 'PROJECT MANAGER',
        course: 'BSIT - 4',
        location: 'BANTUG, ANGADANAN, ISABELA',
        email: '2100834@usl.edu.ph',
        image: '/images/team/jerald-bon-harris-agustin.jpg'
    },
    {
        name: 'JOSEPH KEIRO B. BINALAY',
        initials: 'JB',
        role: 'FULL STACK DEVELOPER',
        course: 'BSIT - 4',
        location: 'CARITAN NORTE, TUGUEGARAO CITY, CAGAYAN',
        email: '2209459@usl.edu.ph',
        image: '/images/team/joseph-keiro-binalay.jpg'
    },
    {
        name: 'KASSANDRA LOUISE G. PAROY',
        initials: 'KP',
        role: 'FULL STACK DEVELOPER',
        course: 'BSIT - 4',
        location: 'UGAC NORTE, TUGUEGARAO CITY, CAGAYAN',
        email: '0800604@usl.edu.ph',
        image: '/images/team/kassandra-louise-paroy.jpg'
    },
    {
        name: 'JUDE ANDREI F. PASICOLAN',
        initials: 'JP',
        role: 'FULL STACK DEVELOPER',
        course: 'BSIT - 4',
        location: 'POBLACION, SAN PABLO, ISABELA',
        email: '1601864@usl.edu.ph',
        image: '/images/team/jude-andrei-pasicolan.jpg'
    }
]);

const adviser = ref({
    name: 'JEROME S. MIGUEL',
    initials: 'JM',
    role: 'ADVISER',
    course: '',
    location: 'SAN JOSE, BAGGAO, CAGAYAN',
    email: 'jeromemiguel@usl.edu.ph',
    image: '/images/team/jerome-miguel.jpg'
});

const instructor = ref({
    name: 'LILY-ANN B. DE LA CRUZ',
    initials: 'LD',
    role: 'INSTRUCTOR',
    course: '',
    location: 'Cataggaman Nuevo, Tuguegarao City, Cagayan',
    email: 'Lilyanndelacruz@usl.edu.ph',
    image: '/images/team/lily-ann-dela-cruz.jpg'
});

onMounted(() => {
    let currentIndex = 0;
    let isTyping = true;
    
    const typeCharacter = () => {
        if (currentIndex < fullText.length) {
            displayedText.value = fullText.substring(0, currentIndex + 1);
            currentIndex++;
            setTimeout(typeCharacter, typingSpeed);
        } else {
            setTimeout(() => {
                isTyping = false;
                eraseCharacter();
            }, pauseAfterTyping);
        }
    };
    
    const eraseCharacter = () => {
        if (currentIndex > 0) {
            currentIndex--;
            displayedText.value = fullText.substring(0, currentIndex);
            setTimeout(eraseCharacter, erasingSpeed);
        } else {
            setTimeout(() => {
                isTyping = true;
                typeCharacter();
            }, pauseAfterErasing);
        }
    };
    
    setTimeout(typeCharacter, 300);

    // Handle smooth scrolling for anchor links
    const handleAnchorClick = (e) => {
        const href = e.target.getAttribute('href');
        if (href && href.startsWith('#')) {
            e.preventDefault();
            const targetId = href.substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    };

    // Add event listeners to all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', handleAnchorClick);
    });

    // Scroll reveal animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal');
                entry.target.style.opacity = '1';
            }
        });
    }, observerOptions);

    // Observe all sections and cards
    const elementsToAnimate = document.querySelectorAll('section, .card-hover');
    elementsToAnimate.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transition = `opacity 0.6s ease-out ${index * 0.1}s, transform 0.6s ease-out ${index * 0.1}s`;
        observer.observe(el);
    });
});
</script>

<style scoped>
@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in-up {
    animation: fade-in-up 0.8s ease-out;
}

@keyframes blink {
    0%, 50% {
        opacity: 1;
    }
    51%, 100% {
        opacity: 0;
    }
}

.typing-cursor {
    display: inline-block;
    animation: blink 1s infinite;
    margin-left: 2px;
}

</style>
