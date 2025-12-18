<template>
    <MainLayout>
        <!-- Hero Section -->
        <section id="home" class="relative overflow-hidden animated-gradient text-white py-24 md:py-32 lg:py-40">
            <!-- Animated Background Elements -->
            <div class="absolute inset-0 overflow-hidden">
                <div
                    class="absolute -top-40 -right-40 w-80 h-80 bg-white opacity-10 rounded-full blur-3xl animate-pulse">
                </div>
                <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-white opacity-10 rounded-full blur-3xl animate-pulse"
                    style="animation-delay: 1s;"></div>
                <div
                    class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-white opacity-5 rounded-full blur-3xl">
                </div>
            </div>

            <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center animate-fade-in-up">
                    <div class="inline-block mb-6">
                        <span
                            class="glass px-4 py-2 rounded-full text-sm font-medium backdrop-blur-md flex items-center gap-2">
                            <Icon name="rocket" :size="16" class="text-white" />
                            Research Platform
                        </span>
                    </div>
                    <h1
                        class="text-6xl md:text-8xl lg:text-9xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-white via-blue-100 to-white">
                        <span>{{ displayedText }}</span><span class="typing-cursor">|</span>
                    </h1>
                    <p
                        class="text-xl md:text-2xl lg:text-3xl mb-10 text-white/90 max-w-3xl mx-auto font-light leading-relaxed">
                        A Tag-Based Career and Training Matching Platform
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                        <a href="https://pathfinder-development-2rbr.onrender.com/" target="_blank"
                            rel="noopener noreferrer"
                            class="group relative px-8 py-4 bg-white text-customButton rounded-xl font-semibold overflow-hidden transition-all duration-300 transform hover:scale-105 shadow-2xl hover:shadow-white/20">
                            <span class="relative z-10">View Pathfinder</span>
                            <div
                                class="absolute inset-0 bg-gradient-to-r from-blue-gray to-white opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            </div>
                        </a>
                        <a href="#features"
                            class="group px-8 py-4 glass border-2 border-white/30 text-white rounded-xl font-semibold backdrop-blur-md hover:bg-white/20 transition-all duration-300 transform hover:scale-105 shadow-xl">
                            Explore Features
                            <span
                                class="inline-block ml-2 transform group-hover:translate-x-1 transition-transform">→</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Scroll Indicator -->
            <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
                <svg class="w-6 h-6 text-white/70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                </svg>
            </div>
        </section>

        <!-- Problem/Solution Split Screen Section -->
        <section id="problem-solution" class="relative py-20 md:py-32 bg-white scroll-mt-16 overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center">
                    <!-- Left Side: The Problem -->
                    <div class="relative">
                        <div
                            class="bg-gradient-to-br from-red-50 via-orange-50 to-red-100 rounded-3xl p-8 md:p-12 border-2 border-red-200 shadow-2xl transform hover:scale-105 transition-transform duration-300">
                            <div
                                class="absolute top-0 right-0 w-32 h-32 bg-red-200/30 rounded-full blur-2xl -mr-16 -mt-16">
                            </div>
                            <div class="relative z-10">
                                <div class="text-center mb-8">
                                    <h2 class="text-4xl md:text-5xl font-extrabold text-red-600 mb-4">
                                        The Problem
                                    </h2>
                                    <div class="inline-block mb-6">
                                        <span
                                            class="text-red-700 text-3xl md:text-4xl font-bold bg-red-100 px-6 py-3 rounded-xl border-2 border-red-300">
                                            Skills Mismatch
                                        </span>
                                    </div>
                                </div>

                                <!-- Disconnect Visual -->
                                <div class="flex items-center justify-center mb-8 py-8">
                                    <div class="relative w-full max-w-md h-32 md:h-40">
                                        <!-- Left side: Job Seeker -->
                                        <div
                                            class="absolute left-0 top-1/2 transform -translate-y-1/2 flex flex-col items-center z-10">
                                            <div
                                                class="bg-white rounded-full p-4 shadow-lg border-4 border-gray-300 mb-2 relative">
                                                <Icon name="user" :size="48" class="text-gray-600" />
                                                <div
                                                    class="absolute -top-1 -right-1 bg-red-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center border-2 border-white">
                                                    !
                                                </div>
                                            </div>
                                            <span
                                                class="text-sm font-bold text-gray-800 bg-white px-3 py-1 rounded-lg border-2 border-gray-300 shadow-sm text-center">Nature
                                                of Job<br /></span>
                                        </div>

                                        <!-- Disconnect Line -->
                                        <div
                                            class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 flex items-center z-0">
                                            <svg class="w-32 md:w-40 h-2 text-red-500" viewBox="0 0 160 8" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <path d="M0 4 L160 4" stroke="currentColor" stroke-width="4"
                                                    stroke-dasharray="8 8" />
                                                <circle cx="80" cy="4" r="6" fill="#EF4444" />
                                            </svg>
                                            <div
                                                class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-full p-1 border-2 border-red-600 shadow-lg">
                                                <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor"
                                                    viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="3" d="M6 18L18 6M6 6l12 12" />
                                                </svg>
                                            </div>
                                        </div>

                                        <!-- Right side: Job -->
                                        <div
                                            class="absolute right-0 top-1/2 transform -translate-y-1/2 flex flex-col items-center z-10">
                                            <div
                                                class="bg-white rounded-full p-4 shadow-lg border-4 border-gray-300 mb-2 relative">
                                                <Icon name="briefcase" :size="48" class="text-gray-600" />
                                                <div
                                                    class="absolute -top-1 -right-1 bg-red-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center border-2 border-white">
                                                    !
                                                </div>
                                            </div>
                                            <span
                                                class="text-sm font-bold text-gray-800 bg-white px-3 py-1 rounded-lg border-2 border-gray-300 shadow-sm">Specialization</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- 64% Statistic -->
                                <div
                                    class="text-center bg-white/80 backdrop-blur-sm rounded-2xl p-6 border-2 border-red-300">
                                    <div class="text-6xl md:text-7xl font-extrabold text-red-600 mb-2">
                                        64%
                                    </div>
                                    <p class="text-lg md:text-xl text-gray-700 font-semibold">
                                        of TVL graduates experience<br />job mismatch
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Right Side: The Solution -->
                    <div class="relative">
                        <div
                            class="bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 rounded-3xl p-8 md:p-12 border-2 border-blue-200 shadow-2xl transform hover:scale-105 transition-transform duration-300">
                            <div
                                class="absolute top-0 left-0 w-32 h-32 bg-blue-200/30 rounded-full blur-2xl -ml-16 -mt-16">
                            </div>
                            <div class="relative z-10">
                                <div class="text-center mb-8">
                                    <h2 class="text-4xl md:text-5xl font-extrabold text-blue-600 mb-4">
                                        The Solution
                                    </h2>
                                </div>

                                <!-- Pathfinder Connection Visual -->
                                <div class="flex items-center justify-center mb-8 py-8 md:py-12">
                                    <div class="relative w-full max-w-md h-40 md:h-48 lg:h-56">
                                        <!-- Left side: Student/Job Seeker -->
                                        <div
                                            class="absolute left-0 top-1/2 transform -translate-y-1/2 flex flex-col items-center z-10">
                                            <div
                                                class="bg-white rounded-full p-4 shadow-lg border-4 border-blue-300 mb-2 animate-pulse relative">
                                                <Icon name="user" :size="48" class="text-blue-600" />
                                                <div
                                                    class="absolute -top-1 -right-1 bg-blue-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center border-2 border-white">
                                                    S
                                                </div>
                                            </div>
                                            <span
                                                class="text-sm font-bold text-gray-800 bg-white px-3 py-1 rounded-lg border-2 border-blue-300 shadow-sm text-center">College
                                                Students<br />or<br>Job Seekers</span>
                                        </div>

                                        <!-- Pathfinder Logo in Center -->
                                        <div
                                            class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 z-20">
                                            <div
                                                class="bg-white rounded-full p-2 md:p-2 shadow-2xl border-4 md:border-6 border-customButton relative">
                                                <img src="/images/logo/Pathfinder_Logo_Transparent.png"
                                                    alt="Pathfinder Logo"
                                                    class="w-20 h-20 md:w-28 md:h-28 lg:w-32 lg:h-32 object-contain" />
                                                <div
                                                    class="absolute -bottom-3 left-1/2 transform -translate-x-1/2 bg-customButton text-white text-sm md:text-base font-bold px-3 py-1.5 rounded-lg whitespace-nowrap border-2 border-white shadow-lg">
                                                    Pathfinder
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Connection Lines -->
                                        <svg class="w-full h-32 absolute left-0 top-1/2 transform -translate-y-1/2 z-0"
                                            viewBox="0 0 400 100" preserveAspectRatio="none">
                                            <path d="M 60 50 L 180 50" stroke="#6682A3" stroke-width="4" fill="none"
                                                stroke-linecap="round" class="animate-pulse" />
                                            <path d="M 220 50 L 340 50" stroke="#6682A3" stroke-width="4" fill="none"
                                                stroke-linecap="round" class="animate-pulse" />
                                            <circle cx="60" cy="50" r="6" fill="#6682A3" />
                                            <circle cx="340" cy="50" r="6" fill="#6682A3" />
                                        </svg>

                                        <!-- Right side: Company -->
                                        <div
                                            class="absolute right-0 top-1/2 transform -translate-y-1/2 flex flex-col items-center z-10">
                                            <div class="bg-white rounded-full p-4 shadow-lg border-4 border-blue-300 mb-2 animate-pulse relative"
                                                style="animation-delay: 0.5s;">
                                                <Icon name="company" :size="48" class="text-blue-600" />
                                                <div
                                                    class="absolute -top-1 -right-1 bg-blue-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center border-2 border-white">
                                                    C
                                                </div>
                                            </div>
                                            <span
                                                class="text-sm font-bold text-gray-800 bg-white px-3 py-1 rounded-lg border-2 border-blue-300 shadow-sm text-center">Organizations</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- Solution Description -->
                                <div
                                    class="text-center bg-white/80 backdrop-blur-sm rounded-2xl p-6 border-2 border-blue-300">
                                    <p class="text-lg md:text-xl text-gray-700 font-semibold mb-2">
                                        Pathfinder bridges the gap
                                    </p>
                                    <p class="text-base text-gray-600">
                                        Connecting college students and job seekers with career opportunities and
                                        trainings through tag-based matching
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>


        <!-- About Section -->
        <section id="about" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle title="About the Research"
                    subtitle="Understanding the background and significance of our project" />

                <!-- Research Background -->
                <div class="mb-16">
                    <div class="bg-gradient-to-r from-blue-gray to-blue-gray rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Research Background</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            The global landscape of hiring is undergoing a transformation, shifting away from a system
                            that prioritizes educational credentials toward one that values demonstrable competency.
                            This "skills-first" paradigm prioritizes knowledge and abilities over formal degrees,
                            designed to expand talent pools and improve how people are matched to jobs.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Despite these shifts, the hiring process is still filled with conflicts. Employers struggle
                            to identify the right talent, often relying on ambiguous and overstuffed job postings that
                            fail to articulate precise requirements. Qualified candidates often get discouraged and
                            preemptively exclude themselves from the application process. This issue is particularly
                            acute in developing economies like the Philippines, which has a documented history of labor
                            mismatch where workers are frequently over-skilled or under-skilled, lacking the requisite
                            competencies for their current roles.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            Statistical data confirms the severity of this structural gap. Approximately 35% of workers
                            in OECD countries are mismatched by qualification. In the Philippines, studies regarding
                            Technical Vocational and Livelihood (TVL) graduates in Butuan City revealed a mismatch
                            incidence of 64%, indicating a severe failure to align educational specialization with
                            employment outcomes. Furthermore, national data indicates that youth unemployment rates have
                            reached 13.5%, more than double the national average.
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
                                When the workforce disconnects from market needs, vulnerable populations suffer the
                                most, facing career trajectories defined by lower lifetime earnings and reduced job
                                satisfaction. On a macroeconomic scale, this skills mismatch serves as a primary driver
                                of productivity loss.
                            </p>
                        </div>
                        <div class="border-l-4 border-customblue pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Zero-Cost Access</h4>
                            <p class="text-gray-600">
                                While digital platforms function as primary intermediaries in the labor market,
                                accessing high-quality training necessary to bridge skill gaps is often financially
                                prohibitive. Pathfinder provides a direct economic intervention by curating zero-cost
                                resources, thereby promoting equity.
                            </p>
                        </div>
                        <div class="border-l-4 border-customdarkblue pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Skills-Based Hiring Benefits</h4>
                            <p class="text-gray-600">
                                Research indicates that non-degreed workers hired into roles based on skills demonstrate
                                a 10-percentage point higher retention rate and realize a 25% salary increase compared
                                to their previous roles. Enabling a genuine skills-based hiring approach is mutually
                                beneficial.
                            </p>
                        </div>
                        <div class="border-l-4 border-customButton pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Centralized Platform</h4>
                            <p class="text-gray-600">
                                The study addresses the need for a centralized platform to access different
                                organizations' training programs that increase job prospects in a competitive job
                                market. By combining various training programs and career opportunities into a
                                user-friendly web application, Pathfinder empowers college students and job seekers.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Problem Statement -->
                <div class="bg-red-50 border-l-4 border-red-500 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Problem Statement</h3>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        Existing workforce technologies, such as machine learning-based career guidance systems, have
                        demonstrated viability in offering tailored career suggestions. However, a critical research gap
                        remains regarding the convergence of functional specificity and economic accessibility. Current
                        platforms often fail to provide a standardized, automated linkage between employer skill demands
                        and cost-free skill acquisition pathways.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        There is a distinct need for systems that enhance "skill signaling," explicitly linking required
                        KSAs (Knowledge, Skills, and Abilities) to recognized credentials, to assist candidates in
                        understanding which skills yield labor market value. Furthermore, many firms that claim to
                        remove degree requirements fail to alter their actual hiring behavior, often because they lack
                        the internal processes to validate skills without educational proxies.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed">
                        While social media platforms and job portals exist, they lack integration with training or skill
                        development resources that are crucial for enhancing an applicant's employability. These systems
                        provide minimal to no support to users when it comes to skill development because they focus
                        heavily on matching applicants with employers. This highlights the need for a unified platform
                        that not only connects users with job opportunities but also empowers them to upskill and
                        prepare through accessible training programs.
                    </p>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section id="features" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle title="System Features" subtitle="Key features and capabilities of our research system" />

                <!-- Features Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
                    <div v-for="(feature, index) in features" :key="index"
                        class="group relative bg-white rounded-2xl p-8 card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden"
                        :style="{ animationDelay: `${index * 0.1}s` }">
                        <div
                            class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500">
                        </div>
                        <div class="relative z-10">
                            <div
                                class="mb-6 transform group-hover:scale-110 group-hover:rotate-6 transition-all duration-300">
                                <div
                                    class="inline-block p-4 rounded-2xl bg-gradient-to-br from-indigo-100 to-purple-100 group-hover:from-indigo-200 group-hover:to-purple-200 transition-all duration-300">
                                    <Icon :name="feature.icon" :size="48" class="text-indigo-600" />
                                </div>
                            </div>
                            <h3
                                class="text-xl font-bold text-gray-900 mb-4 group-hover:text-indigo-600 transition-colors">
                                {{ feature.title }}</h3>
                            <p class="text-gray-600 leading-relaxed">{{ feature.description }}</p>
                        </div>
                        <div
                            class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300">
                        </div>
                    </div>
                </div>

                <!-- System Screenshots Carousel -->
                <div class="mb-16 -mx-4 sm:-mx-6 lg:-mx-8">
                    <div class="w-full bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-50 py-8">
                        <!-- Header with Page Indicator and Navigation -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-4">
                                    <div
                                        class="bg-customButton text-white px-4 py-2 rounded-full font-semibold text-sm">
                                        Page {{ currentScreenshotStep + 1 }} of {{ screenshotSteps.length }}
                                    </div>
                                </div>
                                <div class="flex items-center gap-2">
                                    <button @click="previousScreenshotStep" :disabled="currentScreenshotStep === 0"
                                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor"
                                            viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M15 19l-7-7 7-7" />
                                        </svg>
                                    </button>
                                    <button @click="nextScreenshotStep"
                                        :disabled="currentScreenshotStep === screenshotSteps.length - 1"
                                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor"
                                            viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M9 5l7 7-7 7" />
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
                                        <img :src="currentStepData?.image"
                                            :alt="currentStepData?.title || `Step ${currentScreenshotStep + 1}`"
                                            class="w-full h-auto transition-transform duration-300 ease-in-out group-hover:scale-105"
                                            @error="handleScreenshotError" />
                                    </div>
                                </div>

                                <!-- Right Panel - Description -->
                                <div class="space-y-4">
                                    <p class="text-4xl font-bold text-customButton mb-4">
                                        {{ currentStepData?.description || 'System screenshot showing key functionality.' }}
                                    </p>
                                    <div v-if="currentStepData?.details && currentStepData.details.length > 0"
                                        class="mt-6 space-y-2">
                                        <h3 class="text-xl font-semibold text-gray-800">Key Features:</h3>
                                        <ul class="list-disc list-inside space-y-1 text-gray-600">
                                            <li v-for="(detail, index) in currentStepData.details" :key="index">{{
                                                detail }}</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pagination Dots and Progress Bar -->
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
                            <!-- Pagination Dots -->
                            <div class="flex justify-center items-center gap-3 mb-4 flex-wrap">
                                <button v-for="(step, index) in screenshotSteps" :key="index"
                                    @click="goToScreenshotStep(index)"
                                    class="w-10 h-10 rounded-full border-2 flex items-center justify-center font-semibold text-sm transition-all"
                                    :class="index === currentScreenshotStep
                                        ? 'bg-customButton text-white border-customButton'
                                        : 'bg-white text-gray-700 border-gray-300 hover:border-customButton hover:bg-purple-50'">
                                    {{ index + 1 }}
                                </button>
                            </div>

                            <!-- Progress Bar -->
                            <div class="w-full max-w-4xl mx-auto">
                                <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                                    <div class="h-full bg-customButton transition-all duration-300 ease-out"
                                        :style="{ width: `${((currentScreenshotStep + 1) / screenshotSteps.length) * 100}%` }">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <!-- Additional Features List -->
                <div class="bg-indigo-50 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Additional Features</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div v-for="(item, index) in additionalFeatures" :key="index" class="flex items-center">
                            <svg class="w-6 h-6 text-indigo-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M5 13l4 4L19 7" />
                            </svg>
                            <span class="text-gray-700">{{ item }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>





        <!-- Team Section -->
        <section id="team" class="py-16 bg-gray-50 scroll-mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle title="Our Team" subtitle="The developers and researchers behind this project" />

                <!-- Team Members (Students) - 4 aligned -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
                    <div v-for="(member, index) in students" :key="index"
                        class="group relative bg-white rounded-2xl p-8 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div
                            class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500">
                        </div>
                        <div class="relative z-10">
                            <div
                                class="w-32 h-32 mx-auto mb-6 flex items-center justify-center overflow-hidden rounded-2xl border-4 border-gray-200 group-hover:border-indigo-400 transition-all duration-300 transform group-hover:scale-110 group-hover:rotate-3 shadow-lg">
                                <img v-if="member.image" :src="member.image" :alt="member.name"
                                    class="w-full h-full object-cover" />
                                <div v-else
                                    class="w-full h-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white text-4xl font-bold">
                                    {{ member.initials }}
                                </div>
                            </div>
                            <h3
                                class="text-lg font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">
                                {{
                                    member.name }}</h3>
                            <p class="text-indigo-600 font-semibold mb-2">{{ member.role }}</p>
                            <p class="text-gray-600 text-sm mb-2">{{ member.course }}</p>
                            <p class="text-gray-500 text-xs mb-6">{{ member.location }}</p>
                            <div class="flex justify-center">
                                <a v-if="member.email" :href="`mailto:${member.email}`"
                                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 hover:bg-indigo-600 hover:text-white transition-all duration-300 transform hover:scale-110"
                                    :title="member.email">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Adviser and Instructor - Side by side at the bottom -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-16 max-w-5xl mx-auto">
                    <!-- Adviser -->
                    <div
                        class="group relative bg-white rounded-2xl p-8 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div
                            class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500">
                        </div>
                        <div class="relative z-10">
                            <div
                                class="w-36 h-36 mx-auto mb-6 flex items-center justify-center overflow-hidden rounded-2xl border-4 border-gray-200 group-hover:border-indigo-400 transition-all duration-300 transform group-hover:scale-110 group-hover:rotate-3 shadow-lg">
                                <img v-if="adviser.image" :src="adviser.image" :alt="adviser.name"
                                    class="w-full h-full object-cover" />
                                <div v-else
                                    class="w-full h-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white text-5xl font-bold">
                                    {{ adviser.initials }}
                                </div>
                            </div>
                            <h3
                                class="text-xl font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">
                                {{
                                    adviser.name }}</h3>
                            <p class="text-indigo-600 font-semibold mb-2">{{ adviser.role }}</p>
                            <p class="text-gray-600 text-sm mb-2" v-if="adviser.course">{{ adviser.course }}</p>
                            <p class="text-gray-500 text-xs mb-6">{{ adviser.location }}</p>
                            <div class="flex justify-center">
                                <a v-if="adviser.email" :href="`mailto:${adviser.email}`"
                                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 hover:bg-indigo-600 hover:text-white transition-all duration-300 transform hover:scale-110"
                                    :title="adviser.email">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Instructor -->
                    <div
                        class="group relative bg-white rounded-2xl p-8 text-center card-hover border border-gray-200/50 shadow-lg hover:shadow-2xl overflow-hidden">
                        <div
                            class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/50 transition-all duration-500">
                        </div>
                        <div class="relative z-10">
                            <div
                                class="w-36 h-36 mx-auto mb-6 flex items-center justify-center overflow-hidden rounded-2xl border-4 border-gray-200 group-hover:border-indigo-400 transition-all duration-300 transform group-hover:scale-110 group-hover:rotate-3 shadow-lg">
                                <img v-if="instructor.image" :src="instructor.image" :alt="instructor.name"
                                    class="w-full h-full object-cover" />
                                <div v-else
                                    class="w-full h-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white text-5xl font-bold">
                                    {{ instructor.initials }}
                                </div>
                            </div>
                            <h3
                                class="text-xl font-bold text-gray-900 mb-2 group-hover:text-indigo-600 transition-colors">
                                {{
                                    instructor.name }}</h3>
                            <p class="text-indigo-600 font-semibold mb-2">{{ instructor.role }}</p>
                            <p class="text-gray-600 text-sm mb-2" v-if="instructor.course">{{ instructor.course }}</p>
                            <p class="text-gray-500 text-xs mb-6" v-if="instructor.location">{{ instructor.location }}
                            </p>
                            <div class="flex justify-center">
                                <a v-if="instructor.email" :href="`mailto:${instructor.email}`"
                                    class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 hover:bg-indigo-600 hover:text-white transition-all duration-300 transform hover:scale-110"
                                    :title="instructor.email">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
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
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue';
import { Chart, registerables } from 'chart.js';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';
import Icon from '@/Components/Icon.vue';

Chart.register(...registerables);

const displayedText = ref('');
const fullText = 'Pathfinder';
const typingSpeed = 150;
const erasingSpeed = 100;
const pauseAfterTyping = 2000;
const pauseAfterErasing = 500;

// Process Model
const selectedPhase = ref(null);

const phaseDetails = {
    'requirements': {
        title: 'Requirements Planning',
        description: 'The initial phase of the Rapid Application Development (RAD) methodology where project requirements are gathered, analyzed, and documented. This phase involves stakeholder meetings, user interviews, and requirement specification to establish the foundation for the development process.'
    },
    'user-design': {
        title: 'User Design',
        description: 'The core design phase where user interfaces and system interactions are designed. This phase focuses on creating user-friendly interfaces that meet the requirements established in the planning phase. The design is validated through iterative prototyping, testing, and refinement cycles.'
    },
    'prototype': {
        title: 'Prototype',
        description: 'A working model or mockup of the system is created to visualize and validate design concepts. Prototypes help stakeholders understand the system\'s functionality and provide early feedback for improvements.'
    },
    'test': {
        title: 'Test',
        description: 'The prototype is tested with users and stakeholders to identify usability issues, functional gaps, and areas for improvement. Testing ensures that the design meets user needs and system requirements.'
    },
    'refine': {
        title: 'Refine',
        description: 'Based on testing feedback, the design is refined and improved. This iterative process continues until the design meets all requirements and user expectations, ensuring a high-quality user experience.'
    },
    'construction': {
        title: 'Construction',
        description: 'The actual development phase where the system is built based on the finalized design. Developers implement the features, integrate components, and ensure code quality through best practices and testing.'
    },
    'cutover': {
        title: 'Cutover',
        description: 'The final phase where the system is deployed to production, data is migrated, users are trained, and the system goes live. This phase includes final testing, documentation, and transition from development to operational status.'
    }
};

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

const handleImageError = (event) => {
    console.error('Image failed to load:', event.target.src);
    // Optionally show a fallback or error message
    event.target.style.display = 'none';
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

// Completed objectives used in the conclusion checklist
const conclusionObjectives = ref([
    {
        title: 'Career & training matching web app delivered',
        description: 'Built Pathfinder using the RAD model to automatically match target careers with training posts that share similar tags.'
    },
    {
        title: 'System quality validated (ISO/IEC 25010)',
        description: 'Evaluated with IT experts; all characteristics met the Agree benchmark, confirming the system meets required standards.',
        points: [
            'Functional Suitability',
            'Compatibility',
            'Usability',
            'Security',
            'Portability'
        ]
    },
    {
        title: 'User perception confirmed (USE Questionnaire)',
        description: 'End users strongly agree that the system is useful, satisfying, easy to use, and easy to learn.',
        points: [
            'Usefulness',
            'Satisfaction',
            'Ease of Use',
            'Ease of Learning'
        ]
    }
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

// Chart refs
const endUserPieChart = ref(null);
const itExpertsBarChart = ref(null);

// USE Ratings Data
const useRatings = ref([
    { characteristic: 'Usefulness', mean: '4.63', stars: 5, label: 'Strongly Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Ease of Use', mean: '4.64', stars: 5, label: 'Strongly Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Ease of Learning', mean: '4.51', stars: 5, label: 'Strongly Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Satisfaction', mean: '4.43', stars: 5, label: 'Strongly Agree', animatedValue: 0, animatedFill: 0 }
]);

// ISO Ratings Data
const isoRatings = ref([
    { characteristic: 'Functional Suitability', mean: '4.03', stars: 4, label: 'Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Compatibility', mean: '4.08', stars: 4, label: 'Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Usability', mean: '4.08', stars: 4, label: 'Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Security', mean: '4.00', stars: 4, label: 'Agree', animatedValue: 0, animatedFill: 0 },
    { characteristic: 'Portability', mean: '4.15', stars: 4, label: 'Agree', animatedValue: 0, animatedFill: 0 }
]);

// Overall Rating Data
const overallRating = ref({
    mean: '4.31', // Average of USE (4.55) and ISO (4.07) averages
    stars: 4,
    label: 'Agree',
    animatedValue: 0,
    animatedFill: 0
});

// Computed properties for averages
const useAverage = computed(() => {
    const sum = useRatings.value.reduce((acc, item) => acc + parseFloat(item.mean), 0);
    return sum / useRatings.value.length;
});

const isoAverage = computed(() => {
    const sum = isoRatings.value.reduce((acc, item) => acc + parseFloat(item.mean), 0);
    return sum / isoRatings.value.length;
});

// End User Evaluators Distribution Data
const endUserDistribution = {
    labels: ['College Students (USLT)', 'Job Seekers'],
    data: [21, 13], // Total: 34
    backgroundColor: [
        'rgba(102, 130, 163, 0.8)', // customButton #6682A3
        'rgba(89, 112, 140, 0.8)'   // customblue #59708C
    ],
    borderColor: [
        'rgba(102, 130, 163, 1)', // customButton #6682A3
        'rgba(89, 112, 140, 1)'   // customblue #59708C
    ]
};

// IT Experts Specialization Data
const itExpertsSpecialization = {
    labels: [
        'Junior Programmer',
        'IT Specialist',
        'Project Development Officer I (e-Gov)',
        'Senior Programmer',
        'Database Admin',
        'Programmer Trainee',
        'Computer Maintenance Technologist II',
        'Engineer I',
        'Engineer III'
    ],
    data: [4, 2, 1, 1, 1, 1, 1, 1, 1], // Total: 13
    backgroundColor: [
        'rgba(102, 130, 163, 0.8)', // customButton #6682A3
        'rgba(89, 112, 140, 0.8)',  // customblue #59708C
        'rgba(65, 83, 103, 0.8)',   // customdarkblue #415367
        'rgba(68, 87, 109, 0.8)',   // dark-slate #44576D
        'rgba(107, 125, 143, 0.8)', // chart-4 #6B7D8F
        'rgba(102, 130, 163, 0.6)', // customButton lighter
        'rgba(89, 112, 140, 0.6)',  // customblue lighter
        'rgba(65, 83, 103, 0.6)',   // customdarkblue lighter
        'rgba(68, 87, 109, 0.6)'    // dark-slate lighter
    ],
    borderColor: [
        'rgba(102, 130, 163, 1)', // customButton #6682A3
        'rgba(89, 112, 140, 1)',  // customblue #59708C
        'rgba(65, 83, 103, 1)',   // customdarkblue #415367
        'rgba(68, 87, 109, 1)',   // dark-slate #44576D
        'rgba(107, 125, 143, 1)', // chart-4 #6B7D8F
        'rgba(102, 130, 163, 1)', // customButton
        'rgba(89, 112, 140, 1)',  // customblue
        'rgba(65, 83, 103, 1)',   // customdarkblue
        'rgba(68, 87, 109, 1)'    // dark-slate
    ],
    borderWidth: 1
};

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

onMounted(async () => {
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

    // Initialize charts after DOM is ready
    await nextTick();
    await new Promise(resolve => setTimeout(resolve, 500));

    // Animate USE and ISO ratings
    const animateRatings = () => {
        // Animate USE ratings
        useRatings.value.forEach((item, index) => {
            const targetValue = parseFloat(item.mean);
            const duration = 2000; // 2 seconds
            const steps = 60;
            const increment = targetValue / steps;
            const stepDuration = duration / steps;
            let currentStep = 0;

            const timer = setInterval(() => {
                currentStep++;
                const currentValue = Math.min(increment * currentStep, targetValue);
                item.animatedValue = currentValue;
                item.animatedFill = currentValue;

                if (currentStep >= steps) {
                    clearInterval(timer);
                    item.animatedValue = targetValue;
                    item.animatedFill = targetValue;
                }
            }, stepDuration);
        });

        // Animate ISO ratings with slight delay
        setTimeout(() => {
            isoRatings.value.forEach((item, index) => {
                const targetValue = parseFloat(item.mean);
                const duration = 2000; // 2 seconds
                const steps = 60;
                const increment = targetValue / steps;
                const stepDuration = duration / steps;
                let currentStep = 0;

                const timer = setInterval(() => {
                    currentStep++;
                    const currentValue = Math.min(increment * currentStep, targetValue);
                    item.animatedValue = currentValue;
                    item.animatedFill = currentValue;

                    if (currentStep >= steps) {
                        clearInterval(timer);
                        item.animatedValue = targetValue;
                        item.animatedFill = targetValue;
                    }
                }, stepDuration);
            });
        }, 300);

        // Animate Overall Rating
        setTimeout(() => {
            const targetValue = parseFloat(overallRating.value.mean);
            const duration = 2000; // 2 seconds
            const steps = 60;
            const increment = targetValue / steps;
            const stepDuration = duration / steps;
            let currentStep = 0;

            const timer = setInterval(() => {
                currentStep++;
                const currentValue = Math.min(increment * currentStep, targetValue);
                overallRating.value.animatedValue = currentValue;
                overallRating.value.animatedFill = currentValue;

                if (currentStep >= steps) {
                    clearInterval(timer);
                    overallRating.value.animatedValue = targetValue;
                    overallRating.value.animatedFill = targetValue;
                }
            }, stepDuration);
        }, 600);
    };

    // Start animations when evaluation results section is visible
    const evaluationSection = document.querySelector('.relative.bg-gradient-to-br.from-gray-50.via-indigo-50\\/30.to-purple-50\\/30.rounded-3xl');
    if (evaluationSection) {
        const evaluationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateRatings();
                    evaluationObserver.disconnect();
                }
            });
        }, { threshold: 0.1 });
        evaluationObserver.observe(evaluationSection);

        // Fallback: start animation after a delay if section is already visible
        setTimeout(() => {
            const rect = evaluationSection.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight && rect.bottom > 0;
            if (isVisible) {
                animateRatings();
                evaluationObserver.disconnect();
            }
        }, 1000);
    } else {
        // Fallback: if section not found, start animation anyway
        setTimeout(() => {
            animateRatings();
        }, 1000);
    }

    try {
        // Create Pie Chart for End User Evaluators Distribution
        if (endUserPieChart.value) {
            new Chart(endUserPieChart.value, {
                type: 'pie',
                data: {
                    labels: endUserDistribution.labels,
                    datasets: [{
                        data: endUserDistribution.data,
                        backgroundColor: endUserDistribution.backgroundColor,
                        borderColor: endUserDistribution.borderColor,
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                padding: 15,
                                font: {
                                    size: 12
                                }
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function (context) {
                                    const label = context.label || '';
                                    const value = context.parsed || 0;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${label}: ${value} (${percentage}%)`;
                                }
                            }
                        }
                    }
                }
            });
        }

        // Create Bar Chart for IT Experts Specialization
        if (itExpertsBarChart.value) {
            new Chart(itExpertsBarChart.value, {
                type: 'bar',
                data: {
                    labels: itExpertsSpecialization.labels,
                    datasets: [{
                        label: 'Number of Experts',
                        data: itExpertsSpecialization.data,
                        backgroundColor: itExpertsSpecialization.backgroundColor,
                        borderColor: itExpertsSpecialization.borderColor,
                        borderWidth: itExpertsSpecialization.borderWidth
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: 'y', // Horizontal bar chart
                    scales: {
                        x: {
                            beginAtZero: true,
                            ticks: {
                                stepSize: 1,
                                font: {
                                    size: 11
                                }
                            },
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        y: {
                            ticks: {
                                font: {
                                    size: 15
                                }
                            },
                            grid: {
                                display: false
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function (context) {
                                    return `Experts: ${context.parsed.y}`;
                                }
                            }
                        }
                    }
                }
            });
        }
    } catch (error) {
        console.error('Error creating charts:', error);
    }
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

    0%,
    50% {
        opacity: 1;
    }

    51%,
    100% {
        opacity: 0;
    }
}

.typing-cursor {
    display: inline-block;
    animation: blink 1s infinite;
    margin-left: 2px;
}
</style>
