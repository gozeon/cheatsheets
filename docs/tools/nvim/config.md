## 快速使用

https://github.com/LazyVim/LazyVim

## 配置

see https://github.com/nvim-lua/kickstart.nvim

```lua title="~/.config/nvim/init.lua"
vim.cmd("set number")

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
-- print(lazypath)
vim.opt.rtp:prepend(lazypath)

local plugins = {
	{ "catppuccin/nvim", name= "catppuccin", priority=1000 },
	{
		"nvim-treesitter/nvim-treesitter",
		build =  ":TSUpdate",
		config = function() 
			local configs = require("nvim-treesitter.configs")

			configs.setup({
				ensure_installed = { "vimdoc", "lua", "go", "python", "bash", "erlang", "markdown" },
				sync_install = false,
				highlight = { enable = true },
				indent = { enable = true }
			})
		end
	},
	{
		"nvim-telescope/telescope.nvim", tag = "0.1.5",
		dependencies = { "nvim-lua/plenary.nvim" }
	},
	{
		"windwp/nvim-autopairs",
		event="InsertEnter",
		opts={}
	},
	{
		"nvim-neo-tree/neo-tree.nvim",
		branch="v3.x",
		dependencies = {
			"nvim-lua/plenary.nvim",
			"nvim-tree/nvim-web-devicons",
			"MunifTanjim/nui.nvim",
		}
	},
	{
		"lewis6991/gitsigns.nvim"
	},
	{
		"nvim-lualine/lualine.nvim",
		dependencies = {
			'nvim-tree/nvim-web-devicons'
		}
	},
	{
		"williamboman/mason.nvim"
	},
	{
		"williamboman/mason-lspconfig.nvim"
	},
	{
		"VonHeikemen/lsp-zero.nvim", 
		branch = 'v3.x', 
		lazy = true,
		config = false
	},
	{
		'neovim/nvim-lspconfig',
		dependencies = {
			{ 'hrsh7th/cmp-nvim-lsp' }
		}
	},
	{
		'hrsh7th/nvim-cmp',
		dependencies = {
			{ 'L3MON4D3/LuaSnip' }
		}
	}
}

local opts = {}
-- package manager
require("lazy").setup(plugins, opts)

-- theme
require("catppuccin").setup()
vim.cmd.colorscheme "catppuccin"

-- telescope
vim.g.mapleader="  "
local builtin = require("telescope.builtin")
vim.keymap.set('n', "<leader>ff", builtin.find_files, {})
vim.keymap.set('n', "<leader>fg", builtin.live_grep, {})
--vim.keymap.set('n', "<leader>fb", builtin.buffers, {})
--vim.keymap.set('n', "<leader>fh", builtin.help_tags, {})

-- autopairs
require("nvim-autopairs").setup()

-- gitsigns
require("gitsigns").setup()

-- lualine
require("lualine").setup()

-- lsp
local lsp_zero = require("lsp-zero")
lsp_zero.on_attach(function(client, bufnr)
	lsp_zero.default_keymaps({ buffer = bufnr })
end)

require("mason").setup({})
require("mason-lspconfig").setup({
	handlers = {
		lsp_zero.default_setup
	}
})

require("cmp").setup({})


	

```

