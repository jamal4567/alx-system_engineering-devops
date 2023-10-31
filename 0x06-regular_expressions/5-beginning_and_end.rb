#!/usr/bin/env ruby
# The regular expression that match string.
# string start with h and end with n.
# string can have any single character in between.
puts ARGV[0].scan(/h.n$/).join
