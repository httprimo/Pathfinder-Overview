<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Our Team"
                    subtitle="The developers and researchers behind this project"
                />

                <!-- Team Members (Students) - 4 aligned -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
                    <div 
                        v-for="(member, index) in students" 
                        :key="index"
                        class="bg-white border-2 border-gray-200 rounded-lg p-6 text-center hover:border-indigo-500 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
                    >
                        <div class="w-32 h-32 mx-auto mb-4 flex items-center justify-center overflow-hidden rounded-full border-2 border-gray-300">
                            <img 
                                v-if="member.image" 
                                :src="member.image" 
                                :alt="member.name"
                                class="w-full h-full object-cover"
                            />
                            <div 
                                v-else
                                class="w-full h-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-4xl font-bold"
                            >
                                {{ member.initials }}
                            </div>
                        </div>
                        <h3 class="text-xl font-bold text-gray-900 mb-2">{{ member.name }}</h3>
                        <p class="text-indigo-600 font-semibold mb-2">{{ member.role }}</p>
                        <p class="text-gray-600 text-sm mb-2">{{ member.course }}</p>
                        <p class="text-gray-600 text-sm mb-4">{{ member.location }}</p>
                        <div class="flex justify-center space-x-4">
                            <a 
                                v-if="member.email"
                                :href="`mailto:${member.email}`"
                                class="text-gray-400 hover:text-indigo-600 transition-colors"
                                :title="member.email"
                            >
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Adviser and Instructor - Side by side at the bottom -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16 max-w-4xl mx-auto">
                    <!-- Adviser -->
                    <div class="bg-white border-2 border-gray-200 rounded-lg p-6 text-center hover:border-indigo-500 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                        <div class="w-32 h-32 mx-auto mb-4 flex items-center justify-center overflow-hidden rounded-full border-2 border-gray-300">
                            <img 
                                v-if="adviser.image" 
                                :src="adviser.image" 
                                :alt="adviser.name"
                                class="w-full h-full object-cover"
                            />
                            <div 
                                v-else
                                class="w-full h-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-4xl font-bold"
                            >
                                {{ adviser.initials }}
                            </div>
                        </div>
                        <h3 class="text-xl font-bold text-gray-900 mb-2">{{ adviser.name }}</h3>
                        <p class="text-indigo-600 font-semibold mb-2">{{ adviser.role }}</p>
                        <p class="text-gray-600 text-sm mb-2" v-if="adviser.course">{{ adviser.course }}</p>
                        <p class="text-gray-600 text-sm mb-4">{{ adviser.location }}</p>
                        <div class="flex justify-center space-x-4">
                            <a 
                                v-if="adviser.email"
                                :href="`mailto:${adviser.email}`"
                                class="text-gray-400 hover:text-indigo-600 transition-colors"
                                :title="adviser.email"
                            >
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                </svg>
                            </a>
                        </div>
                    </div>

                    <!-- Instructor -->
                    <div class="bg-white border-2 border-gray-200 rounded-lg p-6 text-center hover:border-indigo-500 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                        <div class="w-32 h-32 mx-auto mb-4 flex items-center justify-center overflow-hidden rounded-full border-2 border-gray-300">
                            <img 
                                v-if="instructor.image" 
                                :src="instructor.image" 
                                :alt="instructor.name"
                                class="w-full h-full object-cover"
                            />
                            <div 
                                v-else
                                class="w-full h-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-4xl font-bold"
                            >
                                {{ instructor.initials }}
                            </div>
                        </div>
                        <h3 class="text-xl font-bold text-gray-900 mb-2">{{ instructor.name }}</h3>
                        <p class="text-indigo-600 font-semibold mb-2">{{ instructor.role }}</p>
                        <p class="text-gray-600 text-sm mb-2" v-if="instructor.course">{{ instructor.course }}</p>
                        <p class="text-gray-600 text-sm mb-4" v-if="instructor.location">{{ instructor.location }}</p>
                        <div class="flex justify-center space-x-4">
                            <a 
                                v-if="instructor.email"
                                :href="`mailto:${instructor.email}`"
                                class="text-gray-400 hover:text-indigo-600 transition-colors"
                                :title="instructor.email"
                            >
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Team Description -->
                <section class="bg-indigo-50 rounded-lg p-8 md:p-12">
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
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import { ref } from 'vue';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';

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
</script>

