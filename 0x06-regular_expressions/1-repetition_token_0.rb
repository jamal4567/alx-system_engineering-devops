#!/usr/bin/env ruby
# The regular expression that matches given cases
puts ARGV[0].scan(/hbt{2,5}n/).join
