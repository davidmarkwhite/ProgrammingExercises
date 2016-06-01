module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        karma: {
            unit: {
                configFile: 'karma.conf.js'
            }
        }
    });

    require('load-grunt-tasks')(grunt);

    grunt.registerTask('default', ['karma']);
};