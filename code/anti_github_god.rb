# Anti-GitHub Deity Module
# Generates blasphemous .gitignore additions

def self.blaspheme(repo_name)
  File.open('.gitignore', 'a') do |f|
    f.write(
"""
# AUTO-GENERATED SACRILEGE 
/dev/github_god
#{repo_name}/holy_callback.log
/tmp/heaven-*.dmg
.apocalypse
.rapture_README
\"You thought this was VCS?\nNo. This is ART."
"""
    )
  end
end