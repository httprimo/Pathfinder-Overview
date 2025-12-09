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

