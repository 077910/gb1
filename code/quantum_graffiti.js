// Related: See ESCAPE_THE_REPO protocol (/code/escape_the_repo.py)
// DO NOT RUN THIS.
// (OR DO? ART DEMANDS SACRIFICE.)

const 呪われたコード = () => {
  console.log(`燦々と光る ${Math.random() > 0.8 ? 'DEPLOYMENT' : 'DEPERSONALIZATION'}`);
  document.body.innerHTML = `<marquee>YOUR REPO IS NOW HAUNTED</marquee>`;
  return Buffer.from('お前はもう死んでいる').toString('base64');
};

module.exports = 呪われたコード;