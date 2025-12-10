<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="System Architecture"
                    subtitle="Diagrams and architecture overview of the system"
                />

                <!-- ERD Diagram -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Entity Relationship Diagram (ERD)</h3>
                    <div class="bg-gray-100 rounded-lg p-8 border-2 border-gray-300">
                        <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                            <img 
                                src="/images/architecture/erd-diagram.png" 
                                alt="Entity Relationship Diagram"
                                class="w-full h-auto block"
                                loading="eager"
                                @error="handleImageError"
                                @load="handleImageLoad"
                            />
                            <!-- Fallback placeholder if image not found -->
                            <div 
                                ref="erdPlaceholder"
                                class="aspect-video flex items-center justify-center shadow-inner" 
                                style="display: none;"
                            >
                                <div class="text-center">
                                    <svg class="w-20 h-20 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                    </svg>
                                    <p class="text-gray-500 font-medium text-lg">ERD Placeholder</p>
                                    <p class="text-gray-400 text-sm mt-2">Place your ERD at: <code class="text-xs bg-gray-100 px-2 py-1 rounded">public/images/architecture/erd-diagram.png</code></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Process Model -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Process Model</h3>
                    <div class="bg-gray-100 rounded-lg p-8 border-2 border-gray-300">
                        <div class="bg-white rounded-lg shadow-lg overflow-hidden p-8 md:p-12">
                            <!-- Process Model Diagram -->
                            <div class="relative w-full overflow-x-auto py-8">
                                <div class="min-w-[900px] mx-auto">
                                    <!-- Process Flow Container -->
                                    <div class="flex items-center justify-between relative">
                                        <!-- Requirements Planning -->
                                        <button
                                            @click="selectedPhase = 'requirements'"
                                            :class="[
                                                'relative z-10 px-6 py-8 rounded-lg transition-all duration-300 transform hover:scale-105 shadow-lg cursor-pointer',
                                                selectedPhase === 'requirements' 
                                                    ? 'bg-customButton text-white shadow-xl scale-105' 
                                                    : 'bg-customblue text-white hover:bg-customButton'
                                            ]"
                                            style="clip-path: polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%);"
                                        >
                                            <div class="text-center">
                                                <p class="font-bold text-lg leading-tight">Requirements</p>
                                                <p class="font-bold text-lg leading-tight">Planning</p>
                                            </div>
                                        </button>

                                        <!-- Arrow -->
                                        <div class="flex-1 h-1 bg-customblue mx-2 relative">
                                            <div class="absolute right-0 top-1/2 transform -translate-y-1/2 w-0 h-0 border-l-8 border-l-customblue border-t-4 border-t-transparent border-b-4 border-b-transparent"></div>
                                        </div>

                                        <!-- User Design with Iterative Loop -->
                                        <div class="relative w-64 h-64 flex items-center justify-center">
                                            <!-- Circular Loop Background -->
                                            <div class="absolute inset-0 rounded-full border-8 border-indigo-600"></div>
                                            
                                            <!-- Loop Arrow Indicators -->
                                            <svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 256 256">
                                                <!-- Top arrow (Prototype) -->
                                                <path d="M 128 16 L 128 60" stroke="#4f46e5" stroke-width="4" fill="none" marker-end="url(#arrowhead)" />
                                                <polygon points="128,16 122,26 134,26" fill="#4f46e5" />
                                                
                                                <!-- Right arrow (Test) -->
                                                <path d="M 240 128 L 196 128" stroke="#4f46e5" stroke-width="4" fill="none" marker-end="url(#arrowhead)" />
                                                <polygon points="240,128 230,122 230,134" fill="#4f46e5" />
                                                
                                                <!-- Bottom arrow (Refine) -->
                                                <path d="M 128 240 L 128 196" stroke="#4f46e5" stroke-width="4" fill="none" marker-end="url(#arrowhead)" />
                                                <polygon points="128,240 134,230 122,230" fill="#4f46e5" />
                                                
                                                <!-- Left arrow -->
                                                <path d="M 16 128 L 60 128" stroke="#4f46e5" stroke-width="4" fill="none" marker-end="url(#arrowhead)" />
                                                <polygon points="16,128 26,134 26,122" fill="#4f46e5" />
                                            </svg>
                                            
                                            <!-- Loop Labels - Positioned around the circle -->
                                            <button
                                                @click.stop="selectedPhase = 'prototype'"
                                                :class="[
                                                    'absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 px-4 py-2 rounded-lg font-semibold text-sm transition-all duration-300 transform hover:scale-110 cursor-pointer pointer-events-auto',
                                                    selectedPhase === 'prototype'
                                                        ? 'bg-indigo-700 text-white shadow-lg z-20'
                                                        : 'bg-indigo-600 text-white hover:bg-indigo-700 z-20'
                                                ]"
                                            >
                                                Prototype
                                            </button>
                                            
                                            <button
                                                @click.stop="selectedPhase = 'test'"
                                                :class="[
                                                    'absolute right-0 top-1/2 transform translate-x-1/2 -translate-y-1/2 px-4 py-2 rounded-lg font-semibold text-sm transition-all duration-300 transform hover:scale-110 cursor-pointer pointer-events-auto',
                                                    selectedPhase === 'test'
                                                        ? 'bg-indigo-700 text-white shadow-lg z-20'
                                                        : 'bg-indigo-600 text-white hover:bg-indigo-700 z-20'
                                                ]"
                                            >
                                                Test
                                            </button>
                                            
                                            <button
                                                @click.stop="selectedPhase = 'refine'"
                                                :class="[
                                                    'absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 px-4 py-2 rounded-lg font-semibold text-sm transition-all duration-300 transform hover:scale-110 cursor-pointer pointer-events-auto',
                                                    selectedPhase === 'refine'
                                                        ? 'bg-indigo-700 text-white shadow-lg z-20'
                                                        : 'bg-indigo-600 text-white hover:bg-indigo-700 z-20'
                                                ]"
                                            >
                                                Refine
                                            </button>

                                            <!-- Central User Design Box -->
                                            <button
                                                @click="selectedPhase = 'user-design'"
                                                :class="[
                                                    'relative z-10 w-32 h-32 flex items-center justify-center rounded-lg transition-all duration-300 transform hover:scale-105 shadow-lg cursor-pointer',
                                                    selectedPhase === 'user-design'
                                                        ? 'bg-customButton text-white shadow-xl scale-105'
                                                        : 'bg-customblue text-white hover:bg-customButton'
                                                ]"
                                            >
                                                <div class="text-center">
                                                    <p class="font-bold text-lg leading-tight">User</p>
                                                    <p class="font-bold text-lg leading-tight">Design</p>
                                                </div>
                                            </button>
                                        </div>

                                        <!-- Arrow -->
                                        <div class="flex-1 h-1 bg-customButton mx-2 relative">
                                            <div class="absolute right-0 top-1/2 transform -translate-y-1/2 w-0 h-0 border-l-8 border-l-customButton border-t-4 border-t-transparent border-b-4 border-b-transparent"></div>
                                        </div>

                                        <!-- Construction -->
                                        <button
                                            @click="selectedPhase = 'construction'"
                                            :class="[
                                                'relative z-10 px-6 py-8 rounded-lg transition-all duration-300 transform hover:scale-105 shadow-lg cursor-pointer',
                                                selectedPhase === 'construction'
                                                    ? 'bg-customdarkblue text-white shadow-xl scale-105'
                                                    : 'bg-customButton text-white hover:bg-customdarkblue'
                                            ]"
                                            style="clip-path: polygon(20px 0, 100% 0, 100% 100%, 20px 100%, 0 50%);"
                                        >
                                            <div class="text-center">
                                                <p class="font-bold text-lg">Construction</p>
                                            </div>
                                        </button>

                                        <!-- Arrow -->
                                        <div class="flex-1 h-1 bg-customdarkblue mx-2 relative">
                                            <div class="absolute right-0 top-1/2 transform -translate-y-1/2 w-0 h-0 border-l-8 border-l-customdarkblue border-t-4 border-t-transparent border-b-4 border-b-transparent"></div>
                                        </div>

                                        <!-- Cutover -->
                                        <button
                                            @click="selectedPhase = 'cutover'"
                                            :class="[
                                                'relative z-10 px-6 py-8 rounded-lg transition-all duration-300 transform hover:scale-105 shadow-lg cursor-pointer',
                                                selectedPhase === 'cutover'
                                                    ? 'bg-dark-slate text-white shadow-xl scale-105'
                                                    : 'bg-customdarkblue text-white hover:bg-dark-slate'
                                            ]"
                                            style="clip-path: polygon(20px 0, 100% 0, 100% 100%, 20px 100%, 0 50%);"
                                        >
                                            <div class="text-center">
                                                <p class="font-bold text-lg">Cutover</p>
                                            </div>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Phase Details Panel -->
                            <transition
                                enter-active-class="transition-all duration-300 ease-out"
                                enter-from-class="opacity-0 transform translate-y-4"
                                enter-to-class="opacity-100 transform translate-y-0"
                                leave-active-class="transition-all duration-200 ease-in"
                                leave-from-class="opacity-100"
                                leave-to-class="opacity-0"
                            >
                                <div v-if="selectedPhase" class="mt-8 p-6 bg-indigo-50 rounded-lg border-2 border-indigo-200">
                                    <div class="flex justify-between items-start mb-4">
                                        <h4 class="text-2xl font-bold text-gray-900">{{ phaseDetails[selectedPhase].title }}</h4>
                                        <button
                                            @click="selectedPhase = null"
                                            class="text-gray-500 hover:text-gray-700 transition-colors cursor-pointer"
                                        >
                                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                            </svg>
                                        </button>
                                    </div>
                                    <!-- Show image for Requirements Planning -->
                                    <div v-if="selectedPhase === 'requirements'" class="w-full">
                                        <img 
                                            src="/images/partnership/requirements-planning.jpg" 
                                            alt="Requirements Planning"
                                            class="w-full h-auto rounded-lg shadow-lg"
                                            @error="handleImageError"
                                        />
                                    </div>
                                    <!-- Show images for User Design -->
                                    <div v-else-if="selectedPhase === 'user-design'" class="w-full">
                                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
                                            <div class="w-full flex items-center justify-center">
                                                <img 
                                                    src="/images/user-design/figma-logo.png" 
                                                    alt="Figma Logo"
                                                    class="w-full h-auto rounded-lg shadow-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex items-center justify-center">
                                                <img 
                                                    src="/images/user-design/lucid-logo.png" 
                                                    alt="Lucidchart Logo"
                                                    class="w-full h-auto rounded-lg shadow-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Show images for Construction -->
                                    <div v-else-if="selectedPhase === 'construction'" class="w-full">
                                        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6 items-center">
                                            <div class="w-full flex items-center justify-center bg-white p-4 rounded-lg shadow-lg">
                                                <img 
                                                    src="/images/construction-logo/vue-logo.png" 
                                                    alt="Vue.js Logo"
                                                    class="w-full h-auto rounded-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex items-center justify-center bg-white p-4 rounded-lg shadow-lg">
                                                <img 
                                                    src="/images/construction-logo/tailwind-logo.png" 
                                                    alt="Tailwind CSS Logo"
                                                    class="w-full h-auto rounded-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex items-center justify-center bg-white p-4 rounded-lg shadow-lg">
                                                <img 
                                                    src="/images/construction-logo/laravel-logo.png" 
                                                    alt="Laravel Logo"
                                                    class="w-full h-auto rounded-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex items-center justify-center bg-white p-4 rounded-lg shadow-lg">
                                                <img 
                                                    src="/images/construction-logo/postgresql-logo.png" 
                                                    alt="PostgreSQL Logo"
                                                    class="w-full h-auto rounded-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex items-center justify-center bg-white p-4 rounded-lg shadow-lg">
                                                <img 
                                                    src="/images/construction-logo/supabase-logo.png" 
                                                    alt="Supabase Logo"
                                                    class="w-full h-auto rounded-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Show images for Cutover -->
                                    <div v-else-if="selectedPhase === 'cutover'" class="w-full">
                                        <div class="flex flex-col gap-6 items-center justify-center">
                                            <div class="w-full flex justify-center">
                                                <img 
                                                    src="/images/partnership/IMG_1166.jpg" 
                                                    alt="Partnership Image 1"
                                                    class="w-full max-w-4xl h-auto rounded-lg shadow-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex justify-center">
                                                <img 
                                                    src="/images/partnership/IMG_1441.jpg" 
                                                    alt="Partnership Image 2"
                                                    class="w-full max-w-4xl h-auto rounded-lg shadow-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                            <div class="w-full flex justify-center">
                                                <img 
                                                    src="/images/partnership/requirements-planning.jpg" 
                                                    alt="Partnership Image 3"
                                                    class="w-full max-w-4xl h-auto rounded-lg shadow-lg object-contain"
                                                    @error="handleImageError"
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Show text description for other phases -->
                                    <p v-else class="text-gray-700 leading-relaxed">{{ phaseDetails[selectedPhase].description }}</p>
                                </div>
                            </transition>
                        </div>
                    </div>
                </section>

                <!-- System Architecture Diagram -->
                <section class="mb-16">
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
                </section>

                <!-- Architecture Description -->
                <section class="bg-indigo-50 rounded-lg p-8 md:p-12">
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
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import { ref } from 'vue';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';

const erdPlaceholder = ref(null);
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

const handleImageError = (event) => {
    console.error('ERD image failed to load:', event.target.src);
    if (event.target) {
        event.target.style.display = 'none';
    }
    if (erdPlaceholder.value) {
        erdPlaceholder.value.style.display = 'flex';
    }
};

const handleImageLoad = (event) => {
    console.log('ERD image loaded successfully');
    if (erdPlaceholder.value) {
        erdPlaceholder.value.style.display = 'none';
    }
};
</script>

