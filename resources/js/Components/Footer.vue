<template>
    <footer class="bg-gray-800 text-white mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- About Section -->
                <div>
                    <h3 class="text-lg font-semibold mb-4">Pathfinder</h3>
                    <p class="text-gray-400 text-sm">
                        A Tag-Based Career and Training Matching Platform
                    </p>
                </div>

                <!-- Quick Links -->
                <div>
                    <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
                    <ul class="space-y-2 text-sm">
                        <li>
                            <a href="/#home" class="text-gray-400 hover:text-white transition-colors">
                                Home
                            </a>
                        </li>
                        <li>
                            <a href="/#about" class="text-gray-400 hover:text-white transition-colors">
                                About
                            </a>
                        </li>
                        <li>
                            <a href="/#features" class="text-gray-400 hover:text-white transition-colors">
                                Features
                            </a>
                        </li>
                        <li>
                            <a href="/#team" class="text-gray-400 hover:text-white transition-colors">
                                Team
                            </a>
                        </li>
                    </ul>
                </div>

                <!-- Contact Section -->
                <div>
                    <h3 class="text-lg font-semibold mb-4">Contact</h3>
                    <p class="text-gray-400 text-sm">
                        Email: judeandrei.f.pasicolan@gmail.com
                    </p>
                </div>
            </div>

            <div class="border-t border-gray-700 mt-8 pt-8 text-center text-sm text-gray-400">
                <p>&copy; {{ new Date().getFullYear() }} Pathfinder. All rights reserved.</p>
            </div>
        </div>
    </footer>
</template>

