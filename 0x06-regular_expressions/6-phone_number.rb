#!/usr/bin/env ruby
# The regular expression that match a 10 digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
