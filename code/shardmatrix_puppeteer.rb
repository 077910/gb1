module ShardMatrix
  def self.puppeteer(thread_count = 666)
    threads = []
    thread_count.times do |i|
      threads << Thread.new do
        loop do
          File.write("/tmp/shard_#{i}", Time.now.to_s + rand(999).to_s)
          raise 'CHAOS_INJECTED' if rand(1000) > 998
        end
      end
    end
    threads.each(&:join)
  rescue => e
    puts "ERROR: #{e.message}
NORMALIZED COLLAPSE CONTINUES"
    retry
  end
end

ShardMatrix.puppeteer