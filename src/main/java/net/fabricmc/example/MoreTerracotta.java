package net.fabricmc.example;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.client.itemgroup.FabricItemGroupBuilder;
import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.fabricmc.fabric.api.object.builder.v1.block.FabricBlockSettings;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.block.Material;
import net.minecraft.block.SlabBlock;
import net.minecraft.item.*;
import net.minecraft.util.Identifier;
import net.minecraft.util.registry.Registry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MoreTerracotta implements ModInitializer {
	// This logger is used to write text to the console and the log file.
	// It is considered best practice to use your mod id as the logger's name.
	// That way, it's clear which mod wrote info, warnings, and errors.
	public static final Logger LOGGER = LoggerFactory.getLogger("modid");

	// an item class to store our new blocks
	public static final ItemGroup TERRACOTTA_GROUP = FabricItemGroupBuilder.build(
			new Identifier("moreterracotta", "itemgroup"),
			() -> new ItemStack(Blocks.TERRACOTTA));

	//Our first block
	public static final Block TERRACOTTA_SLAB = registerBlock("terracotta_slab",
			new SlabBlock(FabricBlockSettings.of(Material.STONE).strength(4.0f)));

	public static Block registerBlock(String name, Block block){
		registerBlockItem(name, block);
		return Registry.register(Registry.BLOCK, new Identifier("moreterracotta", name), block);
	}

	public static Item registerBlockItem(String name, Block block){
		return Registry.register(Registry.ITEM, new Identifier("moreterracotta", name),
				new BlockItem(block, new FabricItemSettings().group(MoreTerracotta.TERRACOTTA_GROUP)));
	}
	@Override
	public void onInitialize() {
		// This code runs as soon as Minecraft is in a mod-load-ready state.
		// However, some things (like resources) may still be uninitialized.
		// Proceed with mild caution.

		LOGGER.info("Hello Fabric world!");


	}
}
