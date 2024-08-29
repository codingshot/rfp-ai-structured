const nearAPI = require('near-api-js');
const { connect, WalletConnection } = nearAPI;
// add vairables for forum contract on testnet
async function initNear() {
  const near = await connect({
    networkId: 'testnet',
    keyStore: new nearAPI.keyStores.BrowserLocalStorageKeyStore(),
    nodeUrl: 'https://rpc.testnet.near.org', // change this to fast NEAR Rpc
    walletUrl: 'https://testnet.mynearwallet.com',
  });

  return new WalletConnection(near);
}

app.post('/submit-rfp', async (req, res) => {
  const { title, description } = req.body;
  const wallet = await initNear();
  try {
    await wallet.account().functionCall({
      contractId: 'forum.potlock.near',
      methodName: 'add_rfp',
      args: {
        name: title,
        description: description,
        submission_deadline: Date.now() + 30 * 24 * 60 * 60 * 1000, // 1 month from now
      },
    });
    res.json({ message: 'RFP submitted successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});